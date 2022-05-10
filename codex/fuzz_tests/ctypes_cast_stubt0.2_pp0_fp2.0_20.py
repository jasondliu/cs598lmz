import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python2
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# python 3 imports
try:
    import urllib.parse as urllib
except ImportError:
    import urllib

# python 3 imports
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# python 3 imports
try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

# python 3 imports
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

# python 3 imports
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# python 3 imports
try:
    from urllib.request import Request
except ImportError:
    from urllib2 import Request

# python 3 imports
try:

