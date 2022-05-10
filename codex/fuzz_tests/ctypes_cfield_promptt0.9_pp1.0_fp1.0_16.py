import ctypes
# Test ctypes.CField.
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int, 2),
                ("z", ctypes.c_int, 3)]
print(X.x.offset, X.y.offset, X.z.offset)
print(X.x._bit_length_, X.y._bit_length_, X.z._bit_length_)
print(X._fields_[0][0])
print(X.y._fields_[0][0])
print(X.z._fields_[0][0])

# Test ctypes.Field.
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int, 2),
                ("z", ctypes.c_int, 3)]
print(X.x.offset, X.y.offset, X.z.offset)
print(X.x._bit_length_, X.y._bit_length_, X.z
