from scrapy.pipelines.files import FilesPipeline
import scrapy
from scrapy import Request
from os.path import splitext
from scrapy.pipelines.images import ImagesPipeline


class BooksImagesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'filename': item.get('file_name')}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        url = request.url
        media_ext = splitext(url)[1]
        return f'full\\{request.meta["filename"]}{media_ext}'


