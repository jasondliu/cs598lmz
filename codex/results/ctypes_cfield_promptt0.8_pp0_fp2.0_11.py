import ctypes
# Test ctypes.CField.

libtest = ctypes.util.find_library("test")
if libtest:
    test = ctypes.CDLL(libtest)
else:
    raise RuntimeError("libtest not found")

# initializations
# test.test_struct_init()

# test fields (in the Python sense)
class StructTest(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_double),
                ("c", ctypes.c_char*10)]

# test initialization
t = StructTest(1, 2.0, "abc")

# check attributes
t.a = 1
t.b = 2.0
t.c = "abc"

# check pointers
test.test_struct_a.restype = ctypes.c_int
test.test_struct_b.restype = ctypes.c_double
test.test_struct_c.restype = ctypes.c_char_p
assert t.a == test.test_struct_a(t)
assert t
