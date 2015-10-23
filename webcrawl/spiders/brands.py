#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import Brands


class BrandsSpider(Spider):
    name = "brands"
    allowed_domains = ["iherb.cn"]
    start_urls = (
        'http://www.iherb.cn/BrandsAZ',
    )

    def parse(self, response):
        sel = Selector(response)
        brands = sel.xpath('//div[@class="spl-row"]/ul[@class="brandListing"]/li/a[@class="black12"]')
        items = []

        for brand in brands:
            item = Brands()
            item['name'] = brand.xpath('text()').extract()
            item['url'] = brand.xpath('@href').extract()
            items.append(item)

        return items
