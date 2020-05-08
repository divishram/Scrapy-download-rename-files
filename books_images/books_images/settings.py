BOT_NAME = 'books_images'

SPIDER_MODULES = ['books_images.spiders']
NEWSPIDER_MODULE = 'books_images.spiders'


ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    'books_images.pipelines.BooksImagesPipeline': 1
}

FILES_STORE = r'downloaded'
# Change this to your path

DOWNLOAD_DELAY = 2
# Change to 0 for fastest crawl
