import codecs
codecs.register_error("strict", codecs.ignore_errors)

class DeprecatedUsage(Exception):
    pass

try:
    # python 3
    from functools import reduce
except ImportError:
    # python 2
    pass

try:
    # python 2 and 3
    unicode
    def is_unicode(s):
        return isinstance(s, unicode)
except NameError:
    # python 3
    def is_unicode(s):
        return isinstance(s, str)

try:
    # python 2 and 3
    from urllib2 import urlopen
except ImportError:
    # python 3
    from urllib.request import urlopen

try:
    # python 2 and 3
    from urllib2 import quote as url_quote
    from urllib2 import unquote as url_unquote
except ImportError:
    # python 3
    from urllib.parse import quote as url_quote
    from urllib.parse import unquote as url_unquote

try:
    # python 2 and 3
    from urll
