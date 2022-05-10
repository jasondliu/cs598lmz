import ctypes
# Test ctypes.CField()

CField = ctypes.CField
StructUnion = ctypes.StructUnion
PyCFuncPtr = ctypes.PyCFuncPtr

class CStruct(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_long),
        ('c', ctypes.c_longlong),
        ('d', ctypes.c_char),
    ]

CStructPtr = ctypes.POINTER(CStruct)

class U(ctypes.Union):
    _fields_ = [
        ('_', CStruct),
        ('e', CStructPtr),
    ]

U.a
U.b
U.c
U.d
U.e


class V(ctypes.Structure):
    _fields_ = [
        ('_', U),
        ('f', U),
        ('g', CStructPtr),
        ('h', CStructPtr),
        ('i', CStructPtr),
        ('j', CStructPtr),
        ('k', CStructPtr),
   
