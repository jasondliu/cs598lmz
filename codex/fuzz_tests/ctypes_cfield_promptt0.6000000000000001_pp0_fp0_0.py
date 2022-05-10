import ctypes
# Test ctypes.CField.from_address
def test_from_address():
    # test the from_address() class method
    class C(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_int),
                    ("c", ctypes.c_int),
                    ("d", ctypes.c_int)]

    c = C(1, 2, 3, 4)
    p = ctypes.pointer(c.c)
    assert ctypes.c_int.from_address(p.value) == c.c
    assert ctypes.c_int.from_address(p.value + ctypes.sizeof(ctypes.c_int)) == c.d
    assert ctypes.CField.from_address(p, C, "c") == c.c
    assert ctypes.CField.from_address(p, C, "d") == c.d
    py.test.raises(ValueError, ctypes.CField.from_address, p, C, "a")
    py.test.raises
