#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import Supplements


class SupplementsSpider(Spider):
    name = "supplements"
    allowed_domains = ["iherb.cn"]
    start_urls = (
        'http://www.iherb.cn/Supplements',
    )

    def parse(self, response):
        sel = Selector(response)
        supplements = sel.xpath('//div[@id="divCategories"]/div[@class="content"]/ul[@class="categories"]/li/a')
        items = []

        for supplement in supplements:
            item = Supplements()
            item['name'] = supplement.xpath('text()').extract()
            item['url'] = supplement.xpath('@href').extract()
            items.append(item)

        return items
