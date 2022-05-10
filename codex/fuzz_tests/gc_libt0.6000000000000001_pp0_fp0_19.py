import gc, weakref
import sys
from threading import local

#===============================================================================
# PY3K:
#===============================================================================

if sys.version_info[0] == 3:
    import codecs
    from io import StringIO
    from itertools import zip_longest
    from functools import reduce
    from io import BytesIO

    import cPickle as pickle
    from urllib.request import urlopen, Request
    from urllib.parse import urlparse, urlunparse, urlencode, quote, unquote
    from urllib.error import HTTPError

    def b(s):
        return s.encode('latin-1')

    def u(s):
        return s

    def iterkeys(d):
        return d.keys()

    def itervalues(d):
        return d.values()

    def iteritems(d):
        return d.items()

    def iterlists(d):
        return d.lists()

    def getargspec(func):
        return inspect.getfullargspec(func)

    def iter
