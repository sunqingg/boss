# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
import time
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

def getCookie():
    COOKIE_DICT = {}
    cookie = "__snaker__id=mW1bv37Qu0Spvc5L; lastCity=101190100; historyState=state; YD00951578218230%3AWM_TID=cB9O1uloId1EFQEEERKQkV9I7Qi9O5%2Br; YD00951578218230%3AWM_NI=cKMdfkqPaeEcAkYuyOxVqlyUtszss%2B8Whae0CLTqSJunGKR46e0j%2B458XHJ%2BN5q4lK74uF5CsWKvP98joyuiKWLnDgUUA3D%2F2u6V5RE7NM2mtdXr9yuIWUWVXQdW2%2BWbNWw%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee94eb6eadb8f9abd27cace78fb7d54a978b8b87c56597f0afb6fb66a1ae82d8f42af0fea7c3b92aa1958385e561b390af86c86983b59796fc45bc8abf8dfc5fb8adb694f221fc89a882e83c81949c92d242b7b289acd140f6bb008baa40f7e898a9c9218eebbfd5ef41f5ecbba7b849b1898597d333fcb6a19af8638989848fc76d978b8fd4c725f2abfab7b85a87e982aeb167b8bc9893bc73b79799b6d65e9c8facb8b12195be82b8f637e2a3; _bl_uid=41ly8t4mw1RcmLbvXxO509Xr77bq; wd_guid=e3e51497-b15b-47cf-a533-2442024e252b; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1716443908; __fid=192ad08e9bd9ce8f558688de4300d495; boss_login_mode=wechat; wt2=DJVUe_SU9Ojdyn1xxLvzXjl-Svdozz3xp_943_Rah1mbQfvWbl5Ayw10aSsYxA7VIyZPB7STiA-x_3f6ZgZ_0lg~~; wbg=0; zp_at=rzjNJ_Lc326P31_ruWjHtaRNR0L5xraMekWmH8AqDeU~; __l=l=%2Fwww.zhipin.com%2Fnanjing%2F&r=&g=&s=3&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1716450699; __c=1716443906; __a=71770825.1677029446.1715328921.1716443906.210.27.23.107; __zp_stoken__=0842fw5fDnVQFOAIBCwMCVlp2fm1OVMK%2FfMK4wr7Co2zCulzCn3VAw4bClENUwrjCmsK4wo9IwqlVwpdkwprCn8K7wrfDvELCnMKTwpvClcKEwpDCnMSmw7zCucWQxKzDssKwwpMyLhcDCAIWe398fnoDFwkDFw4KAQsPAhYFFwM5LMO7YE1HMjQxK0VJQg9PVFtLWksKVUpOPTgIZmcEOCkgwrJ3PDDCtSTCuMOQwrnCu8K1NcK1wrDDhwk9NDA7wrMBKS7CuHkJw4dTF8KyQQjCsyIFRjzDgFVvw4LDrsKyFC1HRsKwxLpGRhpGODI0RzMzMkYqMy3DgVNqw5fDocKzBDcwGDpGRzpGMkZHPDg4Kkc4aSBGPCA0Aw4XCwQjM8K4TMK7w6ZGRw%3D%3D; geek_zp_token=V1RNsnEuD_0ldgXdJoyRkdKiuw7znVxw~~"
    for i in cookie.split("; "):
        j = i.split("=",maxsplit=1)
        COOKIE_DICT[j[0]] =j[1]
    return  COOKIE_DICT


COOKIE_DICT = getCookie()


class BossSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



class BossDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIE_DICT
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # return  response

        driver =  spider.driver
        url = request.url
        driver.get(url)
        time.sleep(random.uniform(5, 10))
        html_text = driver.page_source
        new_response = HtmlResponse(request.url,body=html_text,encoding="utf-8",request=request)

        return new_response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

