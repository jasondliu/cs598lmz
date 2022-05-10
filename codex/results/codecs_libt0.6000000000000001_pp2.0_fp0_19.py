import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import re
import sys
import urllib
import urlparse

from core import config
from core import logger
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "stream"
__category__ = "F,S"
__type__ = "generic"
__title__ = "Stream.to"
__language__ = "IT"

DEBUG = config.get_setting("debug")

host = "http://www.stream.to/"

headers = [
    ['User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'],
    ['Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'],
    ['Accept-Encoding', 'gzip, deflate
