import mmap
import os
import re
import shutil
import sys
import time
import urllib

# Python 3.0 compatibility
try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    from http.cookiejar import CookieJar
except ImportError:
    from cookielib import CookieJar

try:
    from urllib.request import (urlopen, urlretrieve, Request,
                                HTTPCookieProcessor, HTTPRedirectHandler,
                                ProxyHandler)
except ImportError:
    from urllib2 import (urlopen, Request,
                         HTTPCookieProcessor, HTTPRedirectHandler,
                         ProxyHandler)
    from urllib import urlretrieve

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode

try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

