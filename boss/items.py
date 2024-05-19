# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    salary = scrapy.Field()
    address = scrapy.Field()
    job_name = scrapy.Field()
    job_time = scrapy.Field()
    need = scrapy.Field()
    company = scrapy.Field()
    company_info = scrapy.Field()
    skill_tags = scrapy.Field()
