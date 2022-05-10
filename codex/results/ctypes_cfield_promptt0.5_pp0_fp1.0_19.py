import ctypes
# Test ctypes.CField and ctypes.CDataMeta.from_param
from ctypes import *

def test_cfield():
    class X(Structure):
        _fields_ = [("p", POINTER(c_int))]

    class Y(Structure):
        _fields_ = [("x", X)]

    x = X()
    x.p = pointer(c_int(42))
    y = Y()
    y.x = x
    assert y.x.p[0] == 42
    assert y.x.p[0] == 42
    assert y.x.p[0] == 42
    assert y.x.p[0] == 42

def test_from_param():
    class X(Structure):
        _fields_ = [("p", POINTER(c_int))]

    class Y(Structure):
        _fields_ = [("x", X)]

    x = X()
    x.p = pointer(c_int(42))
    y = Y()
    y.x = x
    assert y.x.p[0] ==
