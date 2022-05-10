import gc, weakref

from twisted.python import reflect, failure
from twisted.internet import defer
from twisted.trial import unittest
from twisted.test import proto_helpers

from scrapy.core.downloader.handlers.http11 import HTTP11DownloadHandler
from scrapy.core.downloader.handlers.http11 import ScrapyAgent
from scrapy.core.downloader.handlers.http11 import ScrapyHTTP11DownloadHandler
from scrapy.core.downloader.webclient import _parse
from scrapy.core.downloader.webclient import _parse
from scrapy.core.downloader.handlers.http11 import _parse
from scrapy.http import Headers
from scrapy.responsetypes import responsetypes
from scrapy.utils.test import get_crawler
from scrapy.utils.python import to_unicode


class DownloadHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.spider = object()
        self.crawler = get_crawler(self.spider)
        self.downloader = self.crawler
