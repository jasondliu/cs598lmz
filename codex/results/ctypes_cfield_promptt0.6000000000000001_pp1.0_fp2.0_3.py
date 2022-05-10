import ctypes
# Test ctypes.CField
from ctypes import *

class X(Structure):
    _fields_ = [("name", c_char * 64),
                ("value", c_int)]


class Y(Structure):
    _fields_ = [("name", c_char * 64),
                ("value", c_int)]


class Z(Union):
    _fields_ = [("x", X),
                ("y", Y)]


def test_field_1():
    z = Z()
    z.x.name = b"hello"
    z.x.value = 42
    assert z.x.name == b"hello"
    assert z.x.value == 42
    assert z.y.name == b"hello"
    assert z.y.value == 42

def test_field_2():
    z = Z()
    z.y.name = b"world"
    z.y.value = -1
    assert z.y.name == b"world"
    assert z.y.value == -1
    assert z.x.name == b"world"
   
