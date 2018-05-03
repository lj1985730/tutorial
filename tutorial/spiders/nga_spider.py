# -*- coding: utf-8 -*-

import scrapy


class NgaSpider(scrapy.Spider):
    name = "nga"
    allowed_domains = ["ngacn.cc"]
    start_urls = [
        "http://bbs.ngacn.cc/"
    ]

    def parse(self, response):
        with open("nga.txt", 'wb') as f:
            f.write(response.body)
