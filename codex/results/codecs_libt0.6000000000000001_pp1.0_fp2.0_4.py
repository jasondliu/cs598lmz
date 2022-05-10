import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from w3lib.html import remove_tags
from scrapy import Request
from scrapy.http import TextResponse

from product_spiders.items import Product, ProductLoaderWithoutSpaces as ProductLoader
from product_spiders.utils import extract_price

from product_spiders.base_spiders.primary_spider import PrimarySpider

class BaxSpider(PrimarySpider):
    name = 'bax-music.com'
    allowed_domains = ['bax-shop.nl', 'bax-shop.co.uk', 'bax-shop.com']
    start_urls = ['http://www.bax-shop.nl/', 'http://www.bax-shop.co.uk/', 'http://www.bax-shop.com/']

    csv_file
