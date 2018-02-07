# -*- coding: utf-8 -*-

import scrapy

from crul.items import CrulItem


class BaiduSpider(scrapy.Spider):
    print('=' * 12 + '  Spider  ' + '=' * 12)
    print('> Spider is initing...')
    name = 'baidu'
    allowed_domains = ['baidu.com']
    pages = 6
    start_urls = [('{}' + str(i + 1)).format("http://tieba.baidu.com/p/5538358142?pn=")
                  for i in range(pages)]

    def parse(self, response):
        print('=' * 12 + '  Spider  ' + '=' * 12)
        print('> Spider is parsing...')
        item = CrulItem()
        item['src'] = response.xpath(
            "//img[@class='BDE_Image']/@src").extract()
        yield item
