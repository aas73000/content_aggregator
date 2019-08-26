# -*- coding: utf-8 -*-
import scrapy


class FakingnewsSpider(scrapy.Spider):
    name = 'fakingnews'
    allowed_domains = ['fakingnews.com/']
    start_urls = ['http://fakingnews.com//']

    def parse(self, response):
        yield {"news": response.xpath('//*[@class="top-story-title clear"]/a/text()').get(),
               "url": response.xpath('//*[@class="top-story-title clear"]/a/@href').get()}
        ul = response.xpath('//*[@class="col-lg-3 col-md-4 col-sm-4 hidden-xs"]')
        for i in ul:
            yield {"news": i.xpath('.//a/text()').get(),
                   "url": i.xpath('.//a/@href').get()}


