import ctypes
# Test ctypes.CField
class SimpleCField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

print SimpleCField._fields_

# exception TypeError: item 1 in _fields_ has a duplicate field name
# class CFieldError(ctypes.Structure):
#     _fields_ = [("a", ctypes.c_int),
#                 ("a", ctypes.c_int)]
#
# print CFieldError._fields_

# Test ctypes.Union
class SimpleUnion(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

print SimpleUnion._fields_

# exception TypeError: item 1 in _fields_ has a duplicate field name
# class UnionError(ctypes.Union):
#     _fields_ = [("a", ctypes.c_int),
#                 ("a", ctypes.c_int)]
#
# print UnionError._fields_

# Test Structure
class Simple
