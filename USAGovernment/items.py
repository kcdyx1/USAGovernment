# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NASNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()


class WhiteHouseItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    issue = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()


class DarpaNewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    abstract = scrapy.Field()
    subtitle = scrapy.Field()
    position_office = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()


class DarpaResearchItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    manager = scrapy.Field()
    manager_url = scrapy.Field()
    image_url = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()