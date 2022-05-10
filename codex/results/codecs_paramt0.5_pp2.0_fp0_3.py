import codecs
codecs.register_error('strict', codecs.ignore_errors)

__version__ = '0.9.9'

if sys.version_info[0] < 3:
    from urllib2 import urlopen, Request, URLError
    from urllib import urlencode
    from httplib import IncompleteRead
    from Queue import Queue
    from threading import Thread
    from HTMLParser import HTMLParser
    from urlparse import urlparse
    from cStringIO import StringIO
else:
    from urllib.request import urlopen, Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from http.client import IncompleteRead
    from queue import Queue
    from threading import Thread
    from html.parser import HTMLParser
    from urllib.parse import urlparse
    from io import StringIO


class _Parser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.data =
