import ctypes
# Test ctypes.CFUNCTYPE()

import sys
if sys.platform == "win32":
    from _ctypes import COMError
else:
    COMError = None

from ctypes import *
import _ctypes_test

