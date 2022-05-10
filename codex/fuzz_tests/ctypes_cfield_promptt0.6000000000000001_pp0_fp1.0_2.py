import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int), ('c', ctypes.c_int)]

class S2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_ulong)]

def test_CField():
    s = S()
    s.a = 42
    s.b = 4242
    s.c = 424242
    assert ctypes.sizeof(S) == 12
    assert ctypes.addressof(s.a) == ctypes.addressof(s)
    assert ctypes.addressof(s.b) == ctypes.addressof(s) + 4
    assert ctypes.addressof(s.c) == ctypes.addressof(s) + 8

def test_CField_2():
    s = S2()
    s.a = 42
    s.b = 4242
    assert ctypes.sizeof(S2
