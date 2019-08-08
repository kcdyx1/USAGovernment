# -*- coding: utf-8 -*-
import scrapy
from USAGovernment.items import WhiteHouseItem
from copy import deepcopy


class WhitehouseSpider(scrapy.Spider):
    name = 'whitehouse'
    allowed_domains = ['www.whitehouse.gov']
    start_urls = ['https://www.whitehouse.gov/news/']

    def parse(self, response):
        item = WhitehouseItem()
        #分成每个文章
        article_list = response.xpath('//*[@id="main-content"]/div[2]/div//article')
        for article in article_list:
            item['title'] = article.xpath('./div/h2/a/text()').extract_first()
            item['url'] = article.xpath('./div/h2/a/@href').extract_first()
            item['type'] = article.xpath('./div/p/text()').extract_first()
            item['issue'] = article.xpath('./div/div/div/p/a/text()').extract_first()
            item['time'] = article.xpath('./div/div/p/time/text()').extract_first()
            yield scrapy.Request(
                item['url'],
                callback=self.parse_deeper,
                meta = {'sha': deepcopy(item)}
            )


        next_url_raw = response.xpath('//div[@class="pagination"]/a[@class="pagination__next"]/@href').extract_first()
        if next_url_raw is not None:
            next_url = next_url_raw
        elif next_url_raw is None:
            print("%"*20)
            next_url = "https://www.whitehouse.gov/news/page/" + str(int(response.url.split('/')[-2])+1) + '/'
            print(next_url)
        if next_url != "https://www.whitehouse.gov/news/page/559/":
            print('*'*10 + next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    def parse_deeper(self, response):
        item = response.meta['sha']
        item['content'] = response.xpath('//*[@id="main-content"]/div[2]/div/div//p/text()').extract()
        yield (item)
