# -*- coding: utf-8 -*-
import scrapy


class BbcindiaSpider(scrapy.Spider):
    name = 'bbcindia'
    allowed_domains = ['bbc.com/news/world/asia/india']
    start_urls = ['http://bbc.com/news/world/asia/india/']

    def parse(self, response):
        ul = response.xpath('//*[@class="gel-layout__item gs-u-pb+@m gel-1/3@m gel-1/4@xl gel-1/3'
                            '@xxl nw-o-keyline nw-o-no-keyline@m"]')
        for i in ul:
            news = i.xpath('.//p/text()').get()
            url = response.urljoin(i.xpath('.//a/@href').get())
            yield {"news":news, "url":url}

