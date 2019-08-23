# -*- coding: utf-8 -*-
import scrapy


class UrlCrawlerSpider(scrapy.Spider):
    name = 'url_crawler'
    allowed_domains = ['https://www.freeomovie.com/']
    start_urls = ['http://www.freeomovie.com/']

    def parse(self, response):
        urls = []
        titles = []
        img_urls = []
        for i in response.xpath('//*[@class="boxentry"]'):
            urls.append(i.xpath('a/@href').extract())
            titles.append(i.xpath('a/@title').extract())
            img_urls.append(i.xpath('a/div/img/@src').extract())
        yield {"Titles":titles, "urls":urls, "img_urls":img_urls}
