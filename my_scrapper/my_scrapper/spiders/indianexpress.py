# -*- coding: utf-8 -*-
import scrapy


class IndianexpressSpider(scrapy.Spider):
    name = 'indianexpress'
    allowed_domains = ['https://indianexpress.com/latest-news/']
    start_urls = ['http://indianexpress.com/latest-news//']

    def parse(self, response):
        ul = response.xpath('//*[@class="m-article-landing  m-block-link "]')
        for i in ul:
            url = i.xpath('.//h3/a/@href').get()
            news = i.xpath('.//h3/a/@title').get()
            yield {"news":news, "url":url}

