import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

try:
    ctypes.CFUNCTYPE
except AttributeError:
    raise ImportError("This version of ctypes doesn't support CFUNCTYPE")

import sys
try:
    from ctypes._ctypes_test import func
except ImportError:
    func = None

functype = CFUNCTYPE(c_int, c_int)

# XXX simplification: normally this is a function object
# which is checked using the inspect module.
#
# In unittest terminology, this is a "mock object"
def func(i):
    pass

try:
    callable(func)
except TypeError:
    # Python versions < 2.2
    def callable(obj):
        return hasattr(obj, '__call__')

def check(result, arg):
    if not callable(result):
        raise TypeError("CFUNCTYPE() argument 1 must be callable")
    if not isinstance(arg, (int, long)):
        raise TypeError("CFUNCTYPE
