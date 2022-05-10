import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python2
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

try:
    import thread
except ImportError:
    import _thread as thread

try:
    xrange
except NameError:
    xrange = range

try:
    unicode
except NameError:
    unicode = str

try:
    unichr
except NameError:
    unichr = chr

try:
    basestring
except NameError:
    basestring = str

try:
    long
except NameError:
    long = int

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

