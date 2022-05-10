import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a hack to allow the use of the same code for both Python 2.x
# and Python 3.x.
try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring

# The following is a hack to allow the use of the same code for both Python 2.x
# and Python 3.x.
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

# The following is a hack to allow the use of the same code for both Python 2.x
# and Python 3.x.
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

#
