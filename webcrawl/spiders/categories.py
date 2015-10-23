#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import Categories


class CategoriesSpider(Spider):
    name = "categories"
    allowed_domains = ["iherb.cn"]
    start_urls = (
        'http://www.iherb.cn/Categories',
    )

    def parse(self, response):
        sel = Selector(response)
        categories = sel.xpath('//div[@id="divCategories"]/div[@class="content"]/ul[@class="categories"]/li/a')
        items = []

        for category in categories:
            item = Categories()
            item['name'] = category.xpath('text()').extract()
            item['url'] = category.xpath('@href').extract()
            items.append(item)

        return items
