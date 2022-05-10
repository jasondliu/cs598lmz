import ctypes
# Test ctypes.CField instantiation, and is_field_type()
from ctypes import *
from ctypes.wintypes import *

from ctypes import _pointer_type_cache

# Macros to create simple test structures:
def BUFFER(length):
    return c_char * length

def STRUCT(name, *fields):
    class cls(Structure):
        _fields_ = fields
    cls.__name__ = name
    return cls

def UNION(name, *fields):
    class cls(Union):
        _fields_ = fields
    cls.__name__ = name
    return cls

class TestCase(unittest.TestCase):

    def test_structure_simple(self):
        class X(Structure):
            _fields_ = [("a", c_int)]
        self.assertEqual(sizeof(X), sizeof(c_int))
        self.assertEqual(X.a.offset, 0)

    def test_structure_simple_big(self):
        # To test alignment
        class X(Structure
