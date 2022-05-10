import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Compatible with both Python 2 and 3
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

try:
    from urllib2 import Request
except ImportError:
    from urllib.request import Request

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

try:
    from
