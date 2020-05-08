# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import BooksImagesItem
from urllib.parse import urljoin
from scrapy.loader.processors import MapCompose


class BooksSpider(CrawlSpider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class = 'next']/a")),
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item')

    )

    def parse_item(self, response):
        l = ItemLoader(item=BooksImagesItem(), response=response)
        l.add_xpath('file_name', '//h1/text()',
                    MapCompose(lambda i: i.replace(':', ''))),
        # Files with : were causes errors
        l.add_xpath('file_urls', '//div[@class = "item active"]/img/@src',
                    MapCompose(lambda i: urljoin(response.url, i)))
        # Creates absolute URL
        return l.load_item()
