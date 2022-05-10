import weakref
from twisted.internet import defer, reactor
from twisted.python.failure import Failure
from twisted.python import log
from zope.interface import implements

from scrapy.http import Headers
from scrapy.utils.trackref import object_ref
from scrapy.resolver import dnscache
from scrapy.exceptions import NotConfigured
from scrapy import optional_features
from scrapy.xlib.pydispatch import dispatcher

if 'ssl' in optional_features:
    import OpenSSL


