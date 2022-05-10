import ctypes
# Test ctypes.CField
#
# The test is derived from the ctypes/test/test_cfieldobj.py file,
# by Thomas Heller, Andrew MacIntyre, and Nick Coghlan.

import _ctypes_test

#
# Data for testing the ctypes code
#

STRING_PTR = ctypes.POINTER(ctypes.c_char)

class P(ctypes.Structure):
    _fields_ = [('p', STRING_PTR)]

class Q(ctypes.Structure):
    _fields_ = [('p', P)]

class M(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(ctypes.c_void_p))]

class N(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(M))]

class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_void_p),
                ('c', ctypes.POINTER(ctypes
