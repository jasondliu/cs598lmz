import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["a"]

assert C._fields_[0][0] == ""
assert C._fields_[0][1] is ctypes.c_int
assert C._anonymous_[0] == "a"
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["a"]

assert C._fields_[0][0] == ""
assert C._fields_[0][1] is ctypes.c_int
assert C._anonymous_[0] == "a"
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["a"]

assert C._fields_[0][0] == ""
assert C._fields_[0][1] is ctypes.c_int
assert
