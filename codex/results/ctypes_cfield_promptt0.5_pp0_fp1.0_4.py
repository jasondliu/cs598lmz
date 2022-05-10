import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]
    class D(ctypes.Structure):
        _fields_ = [("j", ctypes.c_int)]
    d = ctypes.CField(D)

print C.d
print C.d.__name__
print C.d.__doc__
print C.d.__module__
print C.d.__class__
print C.d.__dict__
print C.d.__get__(None, C)
print C.d.__get__(C(), C)

# Test ctypes.Field

class C(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]
    class D(ctypes.Structure):
        _fields_ = [("j", ctypes.c_int)]
    d = ctypes.Field(D)

print C.d
print C.d.__name__
print C.d.__doc__
print C.d.__module__

