#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import Products


class ProductsSpider(Spider):
    name = "products"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dhpc&field-keywords=health',
        'http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A3760901%2Ck%3Ahealth&page=2&keywords=health&ie=UTF8&qid=1445391324&spIA=B010KC4E4U,B015JPVGX0',
        'http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A3760901%2Ck%3Ahealth&page=3&keywords=health&ie=UTF8&qid=1445412138&spIA=B0144WXKWO,B0108VF4O2,B010KG2P6K,B010KC4E4U,B015JPVGX0',
        'http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A3760901%2Ck%3Ahealth&page=4&keywords=health&ie=UTF8&qid=1445412151&spIA=B00DEWF63M,B00DFBNKYE,B00CFAZYUO,B0144WXKWO,B0108VF4O2,B010KG2P6K,B010KC4E4U,B015JPVGX0',
        'http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A3760901%2Ck%3Ahealth&page=5&keywords=health&ie=UTF8&qid=1445412177&spIA=B01113TVE0,B010KFUNVU,B010KG2P5G,B00DEWF63M,B00DFBNKYE,B00CFAZYUO,B0144WXKWO,B0108VF4O2,B010KG2P6K,B010KC4E4U,B015JPVGX0',
    )

    def parse(self, response):
        sel = Selector(response)
        prods = sel.xpath('//div[@id="atfResults"]/ul/li')
        items = []

        for prod in prods:
            item = Products()
            item['name'] = prod.xpath('div/div/div/a/h2/text()').extract()
            item['price'] = prod.xpath('div/div/div/a/span/text()').extract()
            item['url'] = prod.xpath('div/div/div/a/@href').extract()[0]
            items.append(item)

        return items
