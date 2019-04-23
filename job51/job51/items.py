# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    table = 'jobs'
    job_title = scrapy.Field()
    company_title = scrapy.Field()
    address = scrapy.Field()
    salary = scrapy.Field()
    big_industry = scrapy.Field()
    school = scrapy.Field()
    year = scrapy.Field()
    company_type = scrapy.Field()
    company_size = scrapy.Field()
    job_url = scrapy.Field()
    recruitment_time = scrapy.Field()

