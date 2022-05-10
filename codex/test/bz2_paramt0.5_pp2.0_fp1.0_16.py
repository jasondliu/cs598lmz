from bz2 import BZ2Decompressor
BZ2Decompressor = None

# Python 2/3 compatibility
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Python 3 compatibility
try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

# Python 3 compatibility
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import ProxyHandler
except ImportError:
    from urllib2 import ProxyHandler

try:
    from urllib.request import build_opener
except ImportError:
    from urllib2 import build_opener

try:
    from urllib.request import install_opener
except ImportError:
    from urllib2 import install_opener

try:
    from urllib.request import Request
except ImportError:
    from urllib2 import Request


class WebParser(HTMLParser):
    """
    WebParser
    """
