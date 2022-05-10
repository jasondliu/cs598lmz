import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
from ctypes.util import find_library

from ctypes import *

if sys.platform == "win32":
    _lib = CDLL(find_library("SDL2"))
