import ctypes
# Test ctypes.CField.
# <rdar://problem/5649966> ctypes.CField doesn't work

if __name__ == "__main__":
    import ctypes.test.test_cfiled
    from ctypes.test.test_cfiled import *

    class X(ctypes.Structure):
        _fields_ = [
            ("foo", ctypes.c_int),
            ("bar", ctypes.c_double),
            ("baz", ctypes.c_char * 10),
            ("arr", ctypes.c_double * 3),
            ("p", ctypes.POINTER(ctypes.c_int)),
            ("s", ctypes.c_char_p),
            ]

    x = X()
    x.foo = 42
    x.bar = 3.14
    x.baz = "spam"
    x.arr[0] = 1.23
    x.arr[1] = 2.34
    x.arr[2] = 3.45
    x.p = ctypes.pointer(ctypes.c_int(99))

