import ctypes

class S(ctypes.Structure):
    x = 5
    _fields_ = [("d", ctypes.c_double),
                ("i", ctypes.c_int),
                ("c", ctypes.c_char),
                ("f", ctypes.c_char),
                ("b", ctypes.c_long),
                ("s", ctypes.c_short)]

def test_buffer():
    # write to a buffer and then read it
    s = S()
    s.d = 1.23
    s.i = -2
    s.c = b"X"
    s.f = b"Y"
    s.b = -3
    s.s = -4

    buf = ctypes.create_string_buffer(ctypes.sizeof(s))
    ctypes.memmove(buf, ctypes.addressof(s), ctypes.sizeof(s))

    s2 = S.from_buffer_copy(buf)
    assert s2.d == 1.23
    assert s2.i == -2
    assert s2.c == b"X"
    assert s
