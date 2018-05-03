# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 企业实体
class EnterpriseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 名称
    corporate = scrapy.Field()  # 法人
    regCapital = scrapy.Field()  # 注册资本
    regTime = scrapy.Field()  # 注册时间
    phoneNo = scrapy.Field()  # 联系电话
    address = scrapy.Field()  # 地址
    scope = scrapy.Field()  # 经营范围
    score = scrapy.Field()  # 分数
    pass
