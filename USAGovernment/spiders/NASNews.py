# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.http import Request
from USAGovernment.items import NASNewsItem

logger = logging.getLogger(__name__)

class NasnewsSpider(scrapy.Spider):
    name = 'NASNews'
    # allowed_domains = ['nas.edu', 'nasonline.org', 'nationalacademies.org']
    start_urls = ['http://www.nas.edu/newsroom/index.html/']


    def parse(self, response):
        for i in response.xpath('//*[@id="newsroom_list"]/table//tr')[:3]:
            if i.xpath('./td/p[1]/font/text()'):
                url = i.xpath('./td/h2/a/@href').extract_first()
                print('-'*3 + url)
                yield scrapy.Request(url, callback=self.parse_deep_content)


    def parse_deep_content(self, response):
        item = NASNewsItem()
        item['title'] = response.xpath('//*[@id="content_int"]/h1/text()').extract_first()
        item['time'] = response.xpath('//*[@id="content_int"]/p[1]/text').extract_first()
        item['content'] = response.xpath('//*[@id="content_int"]/div/p[1]').extract_first()
        print(item)

