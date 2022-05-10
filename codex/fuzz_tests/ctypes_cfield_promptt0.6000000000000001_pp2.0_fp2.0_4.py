import ctypes
# Test ctypes.CFields
class CFields(ctypes.Structure):
    _fields_ = [
        ("b", ctypes.c_byte),
        ("h", ctypes.c_short),
        ("i", ctypes.c_int),
        ("l", ctypes.c_long),
        ("q", ctypes.c_longlong),
        ("f", ctypes.c_float),
        ("d", ctypes.c_double),
        ("b1", ctypes.c_byte),
        ("h1", ctypes.c_short),
        ("i1", ctypes.c_int),
        ("l1", ctypes.c_long),
        ("q1", ctypes.c_longlong),
        ("f1", ctypes.c_float),
        ("d1", ctypes.c_double),
    ]

# Test ctypes.CFields with nested structure
class CFieldsNested(ctypes.Structure):
    _fields_ = [
        ("b", ctypes.c_byte),
        ("nest", CFields),
