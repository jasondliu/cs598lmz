import ctypes
# Test ctypes.CField
class CA(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ]

ca = CA()
ca.a = 1
ca.b = 2
ca.c = 3

CB = CA._fields_[:]
CB[2] = ('d', ctypes.c_int)

class CC(ctypes.Structure):
    _fields_ = CB

cc = CC()
cc.a = 1
cc.b = 2
cc.d = 3

C = CA._fields_[:]
C[1] = ('b', ctypes.c_float)

class CA(ctypes.Structure):
    _fields_ = C

ca = CA()
ca.a = 1
ca.b = 2.
ca.c = 3

CB = CA._fields_[:]
CB[2] = ('d', ctypes.c_float)
class CC(ctypes.Structure):
    _
