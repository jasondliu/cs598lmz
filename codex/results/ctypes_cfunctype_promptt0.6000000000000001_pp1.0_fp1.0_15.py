import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import needs_symbol

################################################################
#
# First, some helper functions:

def dump(obj):
    print(type(obj))
    print(obj)
    print(repr(obj))

def sizeof(typ):
    return ctypes.sizeof(typ)

def alignment(typ):
    return ctypes.alignment(typ)

################################################################
#
# The ctypes type objects:

class _ctypes_test(ctypes._SimpleCData):
    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, super(_ctypes_test, self).__repr__())

class _ctypes_test_2(ctypes._SimpleCData):
    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, super(_ctypes_test_2, self).__repr__())


class _ctypes_test_3(ctypes._SimpleCData):
