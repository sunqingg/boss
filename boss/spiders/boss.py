import time
import random

import scrapy
from lxml import etree
from scrapy import Request
from urllib.parse import urljoin

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from boss.items import BossItem


class BsSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=java%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B"]

    def __init__(self):
        # 创建 ChromeOptions 对象
        chrome_options = Options()

        # 禁用图片加载
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)


        ser = Service()
        ser.path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 替换为实际路径
        # 启动 Chrome 浏览器
        self.driver = webdriver.Chrome(service=ser, options=chrome_options)

    def start_requests(self):
        for i in range(1, 2):
            url = f"https://www.zhipin.com/web/geek/job?query=java%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B&page={i}"
            yield Request(url)

    def parse(self, response):


        # 打开网页
        self.driver.get(response.url)

        # 等待页面加载完成
        time.sleep(random.uniform(4, 10))

        text = self.driver.page_source

        tree = etree.HTML(text)
        # list_jobs = tree.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
        list_jobs = tree.xpath('//div[@class="search-job-result"]/ul[@class="job-list-box"]/li')
        for index, list_job in enumerate(list(list_jobs)):
            boss_item = BossItem()
            print(index, list_job.xpath('.//span[@class="salary"]/text()')[0])
            boss_item["salary"] = list_job.xpath('.//span[@class="salary"]/text()')[0]
            boss_item['address'] = list_job.xpath('.//span[@class="job-area"]/text()')[0]
            boss_item['job_name'] = list_job.xpath('.//span[@class="job-name"]/text()')[0]
            boss_item['skill_tags'] = list_job.xpath('.//div[contains(@class,"job-card-footer")]/ul/li/text()')
            boss_item['job_time'] = list_job.xpath('.//div[contains(@class,"job-info")]/ul/li/text()')
            boss_item['company'] = list_job.xpath('.//h3[@class="company-name"]/a/text()')[0]
            boss_item['company_info'] = list_job.xpath('.//div[contains(@class,"company-info")]/ul/li/text()')

            last_string = list_job.xpath('.//div[contains(@class,"job-card-body")]/a/@href')[0]
            # new_url = self.allowed_domains[0] + last_string
            new_url = response.urljoin(last_string)
            # 执行不是parse方法了
            yield Request(new_url, callback=self.parse_detail, cb_kwargs={'item': boss_item, 'url': new_url})

            yield boss_item
    def parse_detail(self, response, **kwargs):


        boss_item = kwargs['item']
        self.driver.get(kwargs['url'])
        # 等待页面加载完成
        time.sleep(random.uniform(4, 10))
        text = self.driver.page_source

        tree = etree.HTML(text)
        boss_item["need"] = tree.xpath('//div[@class="job-detail-section"]/div[@class="job-sec-text"]/text()')
        yield boss_item

