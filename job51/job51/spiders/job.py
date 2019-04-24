# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import Job51Item


class JobSpider(scrapy.Spider):
    name = 'job'
    # allowed_domains = ['https://www.51job.com/']
    start_urls = ['https://jobs.51job.com/']

    def parse(self, response):
        """解析出行业网址"""
        datas = response.xpath('//div[@class="maincenter"]/div[contains(@class, "filter")][3]/div[contains(@class, "e e5")]')
        for data in datas:
            big_industry = data.xpath('./p/strong/text()').extract_first()  # 大的行业
            # small_industry_titles = data.xpath('./div[@class="lkst"]/a/text()').extract()  # 小行业的名称
            small_industry_urls = data.xpath('./div[@class="lkst"]/a/@href').extract()  # 小行业的网址
            for result in small_industry_urls:
                yield scrapy.Request(url=result, callback=self.parse_industry, meta={'info': big_industry})

    def parse_industry(self, response):
        """更具行业网址解析出岗位网址"""
        item = Job51Item()
        big_industry = response.meta.get('info')
        datas = response.xpath('//div[@class="detlist gbox"]/div[contains(@class, "e")]')
        for data in datas:
            job_url = data.xpath('.//span[@class="title"]/a/@href').extract_first()  # 岗位具体详情页
            job_title = data.xpath('.//span[@class="title"]/a/@title').extract_first()  # 岗位名称
            company_title = data.xpath('.//p[@class="info"]/a/@title').extract_first()  # 公司名称
            address = data.xpath('.//p[@class="info"]//span[contains(@class, "location name")]/text()').extract_first()  # 岗位名称
            salary = data.xpath('.//p[@class="info"]//span[@class="location"]/text()').extract_first()  # 岗位名称
            recruitment_time = data.xpath('.//p[@class="info"]//span[@class="time"]/text()').extract_first()  # 岗位名称
            order_data = data.xpath('.//p[@class="order"]//text()').extract()  # 岗位名称
            order = list(map(lambda x: re.sub(r'\s', '', x), order_data))  # ['学历要求：高中', '|', '工作经验：无工作', '|', '公司性质：民营公司', '|', '公司规模：50-150人']
            school = order[0].split(r'：')[1]
            year = order[2].split(r'：')[1]
            company_type = order[4].split(r'：')[1]
            company_size = order[-1].split(r'：')[1]
            item['big_industry'] = big_industry
            item['job_url'] = job_url
            item['job_title'] = job_title
            item['company_title'] = company_title
            item['address'] = address
            item['salary'] = salary
            item['recruitment_time'] = recruitment_time
            item['school'] = school
            item['year'] = year
            item['company_type'] = company_type
            item['company_size'] = company_size
            yield item
            print('------------'*10)
        next_page = response.xpath('//div[@id="cppageno"]/ul/li[@class="bk"][2]/a/@href').extract_first()  # 翻页
        sicon = response.xpath('//a[@class="sq sicon Dm"]')  # 有内容的网页才有会的节点
        if next_page and sicon:
            print('下一页网址：', next_page)
            yield scrapy.Request(url=next_page, callback=self.parse_industry)
