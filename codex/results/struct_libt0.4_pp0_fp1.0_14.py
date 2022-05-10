import _struct
import _time
import _thread

# Python 2.7 compatibility
try:
    from urllib.parse import urlparse, urlunparse
except ImportError:
    from urlparse import urlparse, urlunparse

# Python 3.x compatibility
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection

# Python 2.x compatibility
try:
    from urllib.request import build_opener
except ImportError:
    from urllib2 import build_opener

# Python 3.x compatibility
try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError

# Python 3.x compatibility
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

# Python 3.x compatibility
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

# Python 3.x compatibility
try:
    from urllib.parse import
