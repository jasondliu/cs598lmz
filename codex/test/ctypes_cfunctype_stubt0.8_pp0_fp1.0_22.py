import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "world"

def test_ctypes():
    assert ffi.string(lib.fun()) == "world"
    assert lib.fun_int() == 42
    assert lib.fun_double() == 3.14
    assert lib.fun_pointer_to_int()[0] == 12345678
    if sizeof(c_int) == 4:
        assert lib.fun_pointer_to_int2()[0] == 0x12345678

def test_call_with_struct():
    assert ffi.string(lib.fun_with_struct(42)) == "42"

def test_call_with_struct_pointer():
    p = ffi.GC(ffi.new("struct point *", {'x': 3, 'y': 4}))
    assert lib.fun_with_struct_pointer(p) == 7
    lib.fun_with_struct_pointer(p)
    assert p.x == 3 and p.y == 4
    p.x = p.y = 5
    assert lib.fun_with_struct_pointer(p)
