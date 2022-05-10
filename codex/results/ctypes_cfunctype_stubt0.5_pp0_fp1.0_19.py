import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun()

#
import ctypes

class MyStructure(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]

def fun(x):
    return MyStructure(x, x+1, x+2)

FUNTYPE = ctypes.CFUNCTYPE(ctypes.POINTER(MyStructure))
fun = FUNTYPE(fun)

print fun(10).contents.x, fun(10).contents.y, fun(10).contents.z

#
import ctypes

class MyStructure(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]

def fun(x):
    return MyStructure(x, x+1, x+2)

FUNTYPE = c
