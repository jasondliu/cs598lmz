import ctypes
# Test ctypes.CField class
import ctypes
class test_cfield(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 10),
                (None, ctypes.c_int), # padding
                ("d", ctypes.c_int)]

assert(test_cfield._fields_ == [("a", ctypes.c_int),
                                ("b", ctypes.c_char * 10),
                                (None, ctypes.c_int), # padding
                                ("d", ctypes.c_int)])

assert(test_cfield.a == 1)
assert(test_cfield.d == 4)

test_cfield.a = 3
assert(test_cfield.a == 3)
assert(test_cfield.d == 4)

test_cfield.d = 6
assert(test_cfield.a == 3)
assert(test_cfield.d == 6)

test_cfield.b = "foo"
assert(test_cfield.b
