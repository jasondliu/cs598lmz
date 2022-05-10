import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert S.x == 'x'
    assert ctypes.c_int == ctypes.c_int
    assert ctypes.c_int != ctypes.c_long

def test_sizeof():
    assert ctypes.sizeof(ctypes.c_int) == 4
    assert ctypes.sizeof(ctypes.c_short) == 2
    assert ctypes.sizeof(ctypes.c_byte) == 1

def test_sizeof_struct():
    assert ctypes.sizeof(S) == 4

def test_c_field_type():
    assert ctypes.c_int == S.x.type

def test_array():
    a = ctypes.c_int * 3
    assert a.__name__ == 'c_int_Array_3'
    assert ctypes.sizeof(a) == 3*4

def test_wintypes():
    assert ctypes.wintypes.BOOL == ctypes.c_long
    assert ctypes.wintypes.BYTE ==
