import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import os

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, HtmlResponse
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.item import Item, Field

from product_spiders.items import Product, ProductLoaderWithNameStrip as ProductLoader

HERE = os.path.abspath(os.path.dirname(__file__))

class TopshopSpider(BaseSpider):
    name = 'topshop.com'
    allowed_domains = ['topshop.com']
    start_urls = ('http://www.topshop.com/',)

    def parse(self, response):
        #categories
        hxs = HtmlXPathSelector(response)        
        categories = hxs.select(u'//ul[@id="navigation"]//a/
