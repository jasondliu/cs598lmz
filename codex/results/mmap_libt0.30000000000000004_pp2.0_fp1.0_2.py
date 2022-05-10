import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from HTMLParser import HTMLParser
from random import randint
from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import get_html
from resources.lib.common import get_html_source
from resources.lib.common import get_html_source_cached
from resources.lib.common import get_html_source_cached_with_headers
from resources.lib.common import get_html_source_with_headers
from resources.lib.common import get_html_source_with_headers_and_cookies
from resources.lib.common import get_html_source_with_headers_and_cookies_with_referer
from resources.lib.common import get_html_source_with_headers_
