import ctypes
# Test ctypes.CFUNCTYPE
try:
    from _ctypes import CFuncPtr
except ImportError:
    CFuncPtr = None

import unittest
