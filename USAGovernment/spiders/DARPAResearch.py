# -*- coding: utf-8 -*-
import scrapy
from USAGovernment.items import DarpaResearchItem
from copy import deepcopy


class DarparesearchSpider(scrapy.Spider):
    name = 'DARPAResearch'
    allowed_domains = ['www.darpa.mil']
    start_urls = ['https://www.darpa.mil/our-research?ppl=view48&PP=0']

    def parse(self, response):
        qian = 'https://www.darpa.mil'
        item = DarpaResearchItem()
        url_list = response.xpath("//*[@class='listing__link']/a/@href").extract()[2:]
        for u in url_list:
            item['url'] = "".join((qian, u))
            yield scrapy.Request(
                item['url'],
                callback=self.parse_deeper,
                meta={'sha': deepcopy(item)}
            )

        page_counter = int(response.url[-1]) + 1
        next_url = response.url[:-1] + str(page_counter)
        if next_url != "https://www.darpa.mil/our-research?ppl=view48&PP=5":
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_deeper(self, response):
        qian = 'https://www.darpa.mil'
        item = response.meta['sha']
        item['title'] = response.xpath('//*[@class="detail__title"]/text()').extract_first()
        item['manager'] = response.xpath('//*[@class="detail__subtitle"]/a/text()').extract_first()
        if response.xpath('//*[@class="detail__subtitle"]/a/@href').extract_first():
            item['manager_url'] = qian + response.xpath('//*[@class="detail__subtitle"]/a/@href').extract_first()
        if response.xpath('//*[@class="detail__image"]/img/@src').extract_first():
            item['image_url'] = qian + response.xpath('//*[@class="detail__image"]/img/@src').extract_first()
        item['content'] = response.xpath('//div[@class="detail__body"]//p/text()').extract()
        item['tags'] = response.xpath('//div[@class="listing__tags detail__tags"]//a/text()').extract()
        yield (item)