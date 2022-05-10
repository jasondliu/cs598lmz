import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)

def f():
    s = S()
    s.x = 10
    return s

# ____________________________________________________________

def test_basic():
    import _ctypes_test
    lib = _ctypes_test.load_library('c_test')
    f = lib.f
    f.argtypes = ()
    f.restype = ctypes.c_void_p
    p = f()
    assert type(p) is ctypes.c_void_p
    assert p.value == 0

def test_array():
    import _ctypes_test
    lib = _ctypes_test.load_library('c_test')
    f = lib.f
    f.argtypes = ()
    f.restype = ctypes.c_void_p
    p = lib.return_array()
    assert type(p) is ctypes.c_void_p
    assert p.value == 0
    p = ctypes.cast(p, ctypes.POINTER(ctypes.c_int))
    assert
