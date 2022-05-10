import ctypes
# Test ctypes.CField
ctypes.CField._fields_ = ('i', ctypes.c_int)

# Test ctypes.CField.__get__()
def test_get():
    class C(ctypes.Structure):
        _fields_ = [("f", ctypes.CField)]
    o = C()
    o.i = 42
    if o.f != 42:
        raise RuntimeError("o.f != 42")
    if C.f.__get__(o) != 42:
        raise RuntimeError("C.f.__get__(o) != 42")
    if C.f != ctypes.CField:
        raise RuntimeError("C.f != ctypes.CField")

# Test ctypes.CField.__set__()
def test_set():
    class C(ctypes.Structure):
        _fields_ = [("f", ctypes.CField)]
    o = C()
    o.f = 42
    o.i = 42
    if o.f != 42:
        raise RuntimeError("o.f != 42")
    if
