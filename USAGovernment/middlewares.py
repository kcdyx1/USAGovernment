# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from faker import Faker

_faker = Faker()


class UserAgentMiddleware():
    # add random user agent
    def process_request(self, request, spider):
        agents = [_faker.firefox(), _faker.opera(), _faker.chrome()]
        request.headers['User-Agent'] = random.choice(agents)