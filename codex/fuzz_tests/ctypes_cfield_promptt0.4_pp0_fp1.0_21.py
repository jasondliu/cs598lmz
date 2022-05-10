import ctypes
# Test ctypes.CField.

class CFoo(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ('d', ctypes.c_int),
    ]

class CTest(ctypes.Structure):
    _fields_ = [
        ('foo', CFoo),
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]

ctypes.CField(CTest, "foo")
ctypes.CField(CTest, "foo.a")
ctypes.CField(CTest, "foo.b")
ctypes.CField(CTest, "foo.c")
ctypes.CField(CTest, "foo.d")
ctypes.CField(CTest, "a")
ctypes.CField(CTest, "b")
ctypes.CField(CTest, "c")

try:
   
