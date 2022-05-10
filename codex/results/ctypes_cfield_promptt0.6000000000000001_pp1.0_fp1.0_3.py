import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

def test_CField():
    x = X()
    assert isinstance(x.a, ctypes.c_int)
    assert isinstance(x.b, ctypes.c_int)

# Test ctypes.CField.from_address(address)

def test_from_address():
    x = X()
    assert x.a == X.a.from_address(id(x))
    assert x.b == X.b.from_address(id(x))

# Test ctypes.addressof()

def test_addressof():
    x = X()
    assert ctypes.addressof(x.a) == ctypes.addressof(x) + ctypes.sizeof(X.a)
    assert ctypes.addressof(x.b) == ctypes.addressof(x) + ctypes.sizeof(X.b)

#
