import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)

def test_lazy_field():
    s = S()
    assert s.x == 1

    s.x = 42
    assert s.x == 42
    assert type(s.x) is ctypes.c_long

def test_field_in_tuple():
    assert (ctypes.c_int(1),) == (1,)
    assert (ctypes.c_int(1),) != (2,)
    assert isinstance((ctypes.c_int(1),), tuple)

def test_field_in_list():
    assert [ctypes.c_int(1)] == [1]
    assert [ctypes.c_int(1)] != [2]
    assert isinstance([ctypes.c_int(1)], list)

def test_struct_in_tuple():
    class S(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

