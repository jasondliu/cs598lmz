import lzma
lzma.LZMAError = KeyError

try:
    from urllib.request import urlopen, ProxyHandler, build_opener, install_opener, Request
    from urllib.error import URLError
except ImportError:
    from urllib2 import urlopen, ProxyHandler, build_opener, install_opener, Request, URLError

try:
    from xml.etree import cElementTree as ElementTree
except ImportError:
    from xml.etree import ElementTree

try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        OrderedDict = dict

try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

try:
    from itertools import izip
except ImportError:
    izip = zip
