import ctypes
# Test ctypes.CField
class c_test(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

c_test_p = ctypes.POINTER(c_test)

c_test_p._fields_ = [("x", ctypes.c_int),
                     ("y", ctypes.c_int)]

# Test ctypes.Field
class c_test2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

c_test2_p = ctypes.POINTER(c_test2)

c_test2_p._fields_ = [("x", ctypes.c_int),
                      ("y", ctypes.c_int)]

# Test ctypes.PField
class c_test3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

c_test3_
