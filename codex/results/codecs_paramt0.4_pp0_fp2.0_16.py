import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 2.x compatibility
try:
    import urllib.request as urllib_request
    import urllib.parse as urllib_parse
    import urllib.error as urllib_error
except ImportError:
    import urllib2 as urllib_request
    import urllib as urllib_parse
    import urllib2 as urllib_error

# Python 3.x compatibility
try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

# Python 2.x compatibility
try:
    from http.cookiejar import CookieJar
except ImportError:
    from cookielib import CookieJar

# Python 3.x compatibility
try:
    from http.client import IncompleteRead
except ImportError:
    IncompleteRead = None

# Python 2.x compatibility
try:
    from urllib.parse import urlparse, urlunparse, unquote, urlencode
except ImportError:
    from urlparse import urlparse, url
