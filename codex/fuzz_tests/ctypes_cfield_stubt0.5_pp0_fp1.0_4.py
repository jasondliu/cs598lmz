import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_init_with_int():
    f = ctypes.CField(42)
    assert f.offset == 42
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.type == ctypes.c_int
    assert f.name == None
    assert f.bits == None
    assert f.pack == 1

def test_cfield_init_with_string():
    f = ctypes.CField("x")
    assert f.offset == None
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.type == ctypes.c_int
    assert f.name == "x"
    assert f.bits == None
    assert f.pack == 1

def test_cfield_init_with_int_string():
    f = ctypes.CField(42, "x")
    assert f.offset == 42
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.type == ctypes.c_
