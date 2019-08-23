# -*- coding: utf-8 -*-
import scrapy


class News18Spider(scrapy.Spider):
    name = 'news18'
    allowed_domains = ['https://news18.com/']
    start_urls = ['http://news18.com/']

    def parse(self, response):
        ul = response.xpath('//*[@id="body-outer"]/footer/div[2]/div[1]/div[2]/ul')
        for i in ul.xpath('.//li'):
            url = i.xpath('.//a/@href').get()
            news = i.xpath('.//a/text()').get()
            yield {'news':news, 'url':url}

