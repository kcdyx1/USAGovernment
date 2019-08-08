# -*- coding: utf-8 -*-
import scrapy
from USAGovernment.items import DarpaNewsItem
from copy import deepcopy


class DarpanewsSpider(scrapy.Spider):
    name = 'DARPAnews'
    allowed_domains = ['www.darpa.mil']
    start_urls = ['https://www.darpa.mil/news?ppl=view48&PP=0']


    def parse(self, response):
        qian = 'https://www.darpa.mil'
        item = DarpaNewsItem()
        url_list = response.xpath("//*[@class='listing__link']/a/@href").extract()
        for u in url_list:
            item['url'] = "".join((qian, u))
            yield scrapy.Request(
                item['url'],
                callback=self.parse_deeper,
                meta={'sha': deepcopy(item)}
            )

        page_counter = int(response.url[-1]) + 1
        next_url = response.url[:-1] + str(page_counter)
        if next_url != "https://www.darpa.mil/news?ppl=view48&PP=10":
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    def parse_deeper(self, response):
        item = response.meta['sha']
        item['title'] = response.xpath('//*[@class="detail__title"]/text()').extract_first()
        item['subtitle'] = response.xpath('//*[@class="detail__newssubtitle"]/text()').extract_first()
        item['position_office'] = response.xpath('//*[@class="detail__position-office"]/text()').extract_first()
        item['date'] = response.xpath('//*[@class="detail__date"]/text()').extract_first()
        item['time'] = response.xpath('//*[@class="detail_time"]/text()').extract_first()
        item['location'] = response.xpath('//*[@class="detail__location"]/text()').extract_first()
        item['address'] = response.xpath('//*[@class="detail__address"]/text()').extract_first()
        item['content'] = response.xpath('//div[@class="detail__body"]//p/text()').extract()
        item['tags'] = response.xpath('//div[@class="listing__tags detail__tags"]//a/text()').extract()
        yield (item)
