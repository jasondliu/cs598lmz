import ctypes
# Test ctypes.CField

if __name__ == "__main__":
    import sys
    import ctypes
    if sys.platform == "win32":
        import _ctypes_test
    else:
        import ctypes.test.test_cfield

    class X(ctypes.Structure):
        _fields_ = [("i", ctypes.c_int),
                    ("f", ctypes.c_float)]

    class Y(ctypes.Structure):
        _fields_ = [("i", ctypes.c_int),
                    ("f", ctypes.c_float)]

    x_p = ctypes.pointer(X())
    y_p = ctypes.pointer(Y())

    x_p[0].i = 2
    x_p[0].f = 3.14
    y_p[0].i = 2
    y_p[0].f = 3.14

    # it's the same instance, the fields are in the same memory
    assert x_p[0].i == y_p[0].i == 2
    assert x_p[0].f
