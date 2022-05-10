from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: None
from cookielib import LWPCookieJar
from dbus.mainloop.glib import DBusGMainLoop
from distutils.version import LooseVersion
from functools import wraps
from multiprocessing.connection import Listener
from optparse import OptionParser
from pycurl import (Curl, CurlMulti,
                    WRITEFUNCTION, WRITEHEADERFUNCTION, MaxRetryException,
                    NOSIGNAL, EAGAIN, MAXREDIRS, RANGE,
                    GLOBAL_SSL, GLOBAL_ACK_EINTR, GLOBAL_ALL)
from threading import Event
from urlparse import urljoin
from xml.etree.ElementTree import fromstring
from xml.parsers.expat import ExpatError
from xml.sax import handler, parseString
from xml.sax.saxutils import XMLGenerator
from zlib import MAX_WBITS
from zlib import decompressobj as zlib_decompressobj

try:
    import urllib2
    import checksum
except ImportError, e
