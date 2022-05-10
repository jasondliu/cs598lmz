import ctypes
# Test ctypes.CField
import ctypes

class X(ctypes.Structure):
    pass

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    pass

class W(ctypes.Structure):
    _fields_ = [("z", Z)]

class V(ctypes.Structure):
    _fields_ = [("y", Y),
                ("w", W)]

def test_ctypes_field():
    x = X()
    x.value = 42
    y = Y()
    y.x = x
    z = Z()
    z.value = 43
    w = W()
    w.z = z
    v = V()
    v.y = y
    v.w = w
    assert v.y.x.value == 42
    assert v.w.z.value == 43
    v.y.x.value = 44
    v.w.z.value = 45
    assert v.y.x.value == 44
    assert v.w.z
