# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class BooksImagesItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field(
        output_processor=TakeFirst()
    )