import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class C2(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

class C3(ctypes.Structure):
    _fields_ = [("c", C), ("c2", C2)]

c = C3()
c.c.x = 1
c.c2.y = 2
print c.c.x, c.c2.y

# Test ctypes.CArray
class C4(ctypes.Structure):
    _fields_ = [("arr", ctypes.c_int * 3)]

c4 = C4()
c4.arr[0] = 1
c4.arr[1] = 2
c4.arr[2] = 3
print c4.arr[0], c4.arr[1], c4.arr[2]

# Test ctypes.CString
class C5(ctypes.Structure):
    _fields_ = [("str", c
