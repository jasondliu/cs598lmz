import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

assert X._fields_[0][0] == "a"
assert X._fields_[0][1] == ctypes.CField
assert X._fields_[0][2] == 0
assert X._fields_[0][3] is None

# Test ctypes.CField(ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField(ctypes.c_int))]

assert X._fields_[0][0] == "a"
assert X._fields_[0][1] == ctypes.CField(ctypes.c_int)
assert X._fields_[0][2] == 0
assert X._fields_[0][3] is None

# Test ctypes.CField(ctypes.c_int, 1)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField(ctypes.c_
