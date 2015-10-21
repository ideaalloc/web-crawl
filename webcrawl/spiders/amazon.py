# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import WebcrawlItem


class AmazonSpider(Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dhpc&field-keywords=health',
        'http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A3760901%2Ck%3Ahealth&page=2&keywords=health&ie=UTF8&qid=1445391324&spIA=B010KC4E4U,B015JPVGX0',
    )

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]')
        items = []

        for site in sites:
            item = WebcrawlItem()
            item['url'] = site.xpath('@href').extract()
            item['description'] = site.xpath('h2/text()').extract()
            items.append(item)

        return items
