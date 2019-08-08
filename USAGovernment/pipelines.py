# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import logging
#
# logger = logging.getLogger(__name__)

collection_wh = client['whitehouse']['news']
collection_dn = client['darpa']['news']
collection_dr = client['darpa']['research']


class UsagovernmentPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "whitehouse":
            collection_wh.insert(dict(item))
            # print(item)

        elif spider.name == "DARPAnews":
            collection_dn.insert(dict(item))

        elif spider.name == "DARPAResearch":
            collection_dr.insert(dict(item))
            # print(item)

        return item
