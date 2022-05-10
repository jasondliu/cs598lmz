import ctypes
# Test ctypes.CField_Type.from_address
if ctypes.sizeof(ctypes.c_int) == 4:
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    class Y(ctypes.Structure):
        _fields_ = [("b", ctypes.c_int)]
    x = X()
    x.a = 1234
    y = Y.from_address(ctypes.addressof(x))
    assert y.b == 1234

# Test ctypes.CField_Type.from_buffer
if ctypes.sizeof(ctypes.c_int) == 4:
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    class Y(ctypes.Structure):
        _fields_ = [("b", ctypes.c_int)]
    x = X()
    x.a = 1234
    y = Y.from_buffer(x)
    assert y.b == 1234

# Test ctypes.CField_
