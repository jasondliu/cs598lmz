import ctypes
# Test ctypes.CFUNCTYPE()
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@CFuncPtr
def my_callback(x, y):
    return x * y

my_callback(2, 3)

# Test ctypes.POINTER()
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

PointArray = POINT * 3
pa = PointArray()
for i in range(3):
    pa[i].x = i
    pa[i].y = i

pa_pointer = ctypes.POINTER(ctypes.POINTER(POINT))
