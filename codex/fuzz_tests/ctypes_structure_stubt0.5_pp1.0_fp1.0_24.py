import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def test_ctypes_struct():
    s = S()
    s.x = 1
    s.y = 2
    assert s.x == 1
    assert s.y == 2

def test_ctypes_struct_addr():
    s = S()
    s.x = 1
    s.y = 2
    addr = ctypes.addressof(s)
    assert addr == s.__ctypes_from_address__(addr)

def test_ctypes_struct_addr_offset():
    s = S()
    s.x = 1
    s.y = 2
    addr = ctypes.addressof(s)
    assert addr+4 == s.__ctypes_from_address__(addr+4)

def test_ctypes_struct_addr_offset_read():
    s = S()
    s.x = 1
    s.y = 2
    addr = ctypes.addressof(s)
    s2 = s.__ctypes
