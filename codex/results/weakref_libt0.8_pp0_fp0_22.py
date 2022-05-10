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


class ConnectionManager(object_ref):
    """A ConnectionManager keeps track of the open connections of a Crawler and
    handles how to acquire them.

    Once initialised it should be used like::

        with crawler.connection_manager as connman:
            yield conn.get_connection('www.example.com', 80, scheme='http')

    It's possible to request a connection by domain::

        conn = connman.get_connection('www.example.com')

    Or by (domain, port) pair::

        conn = connman.get_connection('www.example.com',
