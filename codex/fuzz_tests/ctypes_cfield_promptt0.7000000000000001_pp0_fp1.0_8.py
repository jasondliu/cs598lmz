import ctypes
# Test ctypes.CField
_fields_ = [
    ("a", ctypes.c_int),
    ("b", ctypes.c_int),
    ("c", ctypes.c_int),
    ("d", ctypes.c_int),
    ("e", ctypes.c_int),
    ("f", ctypes.c_int),
    ("g", ctypes.c_int),
    ("h", ctypes.c_int),
    ("i", ctypes.c_int),
    ("j", ctypes.c_int),
    ("k", ctypes.c_int),
    ("l", ctypes.c_int),
]
class A(ctypes.Structure):
    _fields_ = _fields_

a = A()
a.a = 1
print("a.a =", a.a)

# Test ctypes.c_field
_fields_ = [
    ("a", ctypes.c_int),
    ("b", ctypes.c_int),
    ("c", ctypes.c_int),
    ("d", ctypes.c
