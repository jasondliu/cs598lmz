import ctypes
# Test ctypes.CFUNCTYPE()

import sys
import inspect

from ctypes import *

if sys.platform == "win32":
    libc = cdll.msvcrt
else:
    libc = cdll.LoadLibrary(None)

