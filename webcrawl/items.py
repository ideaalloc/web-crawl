# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Products(Item):
    name = Field()
    price = Field()
    url = Field()


class Details(Item):
    spec_names = Field()
    spec_values = Field()
    brand = Field()
    desc = Field()
    pic = Field()
    comments = Field()
    url = Field()
