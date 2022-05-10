import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', ctypes.c_int), ('c', ctypes.c_char)]

class D(ctypes.Structure):
    _fields_ = [('s', ctypes.c_int), ('c', ctypes.c_char), ('i', ctypes.c_int)]

def test_C_sizeof():
    assert sizeof(C) == 2

def test_C_from_buffer():
    buf = buffer(bytearray(b"\x01\x02"))
    c = C.from_buffer(buf)
    assert c.s == 0x01
    assert c.c == b"\x02"

def test_C_from_buffer_write():
    buf = buffer(bytearray(b"\x01\x02"))
    c = C.from_buffer(buf)
    c.s = 0x02
    c.c = b"\x01"
    assert buf == bytearray(b"\x02\x01
