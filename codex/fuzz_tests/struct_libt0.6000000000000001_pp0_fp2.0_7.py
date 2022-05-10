import _struct
import _sys
import _time
import _urllib
import _urllib2
import _urlparse
import _uuid
import _warnings
import _weakref
import _webbrowser
import _xml
import _xmlrpclib

# Some modules have a different name in Python 2.
# These aliases allow the same source to be used in both versions.
_osx_support = _imp.load_dynamic(__name__, '_osx_support')
_scproxy = _imp.load_dynamic(__name__, '_scproxy')
_scproxy._osx_support = _osx_support

# These modules are here for backwards compatibility.
# They used to live in the _osx_support module.
_osx_support._cf = _cf
_osx_support._ctypes = _ctypes
_osx_support._ctypes_test = _ctypes_test
_osx_support._ctypes_test_threads = _ctypes_test_threads
_osx_support._heapq = _heap
