import ctypes
# Test ctypes.CField.
import ctypes._testcapi

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_long),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_char * 4),
        ("e", ctypes.c_long),
    ]

if ctypes.sizeof(X) != 24:
    raise Exception("sizeof(X) == %d, expected 24" % (ctypes.sizeof(X),))

x = X()
x.a = 0x12345678
x.b = 2
x.c = 3
x.d = b"abcd"
x.e = 0x87654321

if ctypes._testcapi.test_cfield(x) != 0:
    raise Exception("ctypes._testcapi.test_cfield() failed")

if x.a != 0x12345678:
    raise Exception("x.a changed")
if x.b != 2:
    raise
