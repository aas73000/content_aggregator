# -*- coding: utf-8 -*-
import scrapy


class NdtvSpider(scrapy.Spider):
    name = 'ndtv'
    allowed_domains = ['ndtv.com/']
    start_urls = ['http://ndtv.com//']

    def parse(self, response):
        ul = response.xpath("/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/ul")#getting the tag <ul>
        for i in ul.xpath(".//li"):
            news = i.xpath(".//h2/a")[1].xpath(".//text()").get()#genrate the title of the news
            url = i.xpath(".//h2/a")[1].xpath(".//@href").get()#generate all urls of top news
            yield {"news":news,"url":url}
