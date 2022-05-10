import ctypes
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
x = X()
x.a = 42
addr = ctypes.addressof(x)
Xp = ctypes.POINTER(X)
y = Xp.from_address(addr)
y.contents.a
