import ctypes
# Test ctypes.CField
#
# This should work if you have a C compiler

import unittest
import ctypes
os = ctypes

testdll = ctypes.CDLL("testdll")

class X(ctypes._SimpleCData):
    _type_ = "i"
    def __init__(self, value):
        self.value = value

FORMAT = "bBhHiIlLdf"

def do_test_struct_fields(self):

    class X(ctypes._StructField):
        _ctype_ = "i"

        def __setattr__(self, name, value):
            if name != "value":
                raise NameError("no such field")
            ctypes._StructField.__setattr__(self, name, value)

    class Y(ctypes._StructField):
        _ctype_ = "i"
        def __setattr__(self, name, value):
            # test the lack of self.value
            ctypes._StructField.__setattr__(self, name, value)

    # XXX This one is redundant, should remove it
