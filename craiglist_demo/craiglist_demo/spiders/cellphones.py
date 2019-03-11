# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
#from craiglist_demo.craiglist_demo import items

class CellphoneSpider(scrapy.Spider):
    name = 'cellphone'
    allowed_domains = ['chicago.craigslist.org']
    start_urls = ['https://chicago.craigslist.org/d/cell-phones/search/moa']

    def parse_lower(self,response):
        ads = response.xpath('//li[@class="result-row"]')
        for ad in ads:
            title = ad.xpath('p/a/text()').extract_first()
            link = ad.xpath('p/a/@href').extract_first()

            yield {'Title': title, 'Link': link}

    def parse(self, response):
        ads = response.xpath('//li[@class="result-row"]')
        for ad in ads:
            title = ad.xpath('p/a/text()').extract_first()
            link = ad.xpath('p/a/@href').extract_first()

            yield {'Title':title,'Link':link}

        next_rel_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = response.urljoin(next_rel_url)
        yield Request(next_url, callback=self.parse)

