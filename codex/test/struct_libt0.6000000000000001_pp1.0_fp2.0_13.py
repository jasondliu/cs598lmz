import _struct
import _ctypes
from ctypes import *
from ctypes import __version__

if __version__ < "1.0.1":
    raise Exception("ctypes %s is too old" % __version__)

from ctypes import util

import sys
if sys.platform == "win32":
    from _ctypes import FreeLibrary as _dlclose
else:
    from _ctypes import dlclose as _dlclose

from _ctypes import LoadLibrary as _dlopen
from _ctypes import GetProcAddress as _dlsym

def _dlopen(name):
    if name is None:
        return None
    if not isinstance(name, str):
        raise TypeError("argument 1 must be string, not %s" % (type(name),))
    name = _dlopen(name)
    if name is None:
        raise OSError("could not open %s" % name)
    return name

# This is a list of all the functions which are imported from the
# _ctypes extension module.  It is used in __del__ methods of
