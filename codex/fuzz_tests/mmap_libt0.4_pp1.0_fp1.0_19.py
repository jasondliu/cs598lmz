import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2

from optparse import OptionParser

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

from pygaga.helpers.logger import log_init
from pygaga.helpers.dbutils import get_db_engine
from pygaga.helpers.urlutils import download, parse_html

from guang_crawler.taobao_shop_item_parser import parse_taobao_shop_item_page

logger = logging.getLogger('CrawlLogger')

DEFAULT_UA = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"

def crawl_taobao_shop_item(shop_id, shop_name, url, shop_item_id, shop_item_name, shop_item_price, shop_item_sales):
    try:
        url = url.replace("http://", "")
       
