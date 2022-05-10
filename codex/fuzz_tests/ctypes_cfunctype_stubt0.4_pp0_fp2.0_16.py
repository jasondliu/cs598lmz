import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "abc"

def test_ctypes_cfuntype():
    assert fun() == "abc"

def test_ctypes_pointer():
    p = ctypes.pointer(ctypes.c_int(42))
    assert p[0] == 42
    p[0] = 43
    assert p[0] == 43

def test_ctypes_byref():
    x = ctypes.c_int(42)
    p = ctypes.byref(x)
    assert type(p) is ctypes.POINTER(ctypes.c_int)
    assert p[0] == 42
    p[0] = 43
    assert p[0] == 43

def test_ctypes_string_at():
    s = ctypes.create_string_buffer(b"hello world")
    assert ctypes.string_at(s) == b"hello world"
    assert ctypes.string_at(s, 5) == b"hello"
    assert ctypes.string_at(s, 5, 1) == b"ello"
    assert c
