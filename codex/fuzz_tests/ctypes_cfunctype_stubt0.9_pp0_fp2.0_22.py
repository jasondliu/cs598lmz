import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('fun')
import ctypes 
import math
lib = ctypes.cdll.LoadLibrary('./libmymath.so')
r = math.sqrt
print(r)

# lib.factorial.restype = ctypes.c_double
# lib.factorial.argtypes = [ctypes.c_int, ctypes.c_int]
lib.factorial.argtypes = [ctypes.c_double]
lib.factorial.restype = ctypes.c_double
# r = lib.factorial(2, 6)
r = lib.factorial(15)
print(r)

def fun(x):
    print(x)
    return x

fun(1)
print(type(fun))

def fun(x):
    print(x)
    return x

f = fun(2)
print(f)
print(f is None)
import ctypes
def fun(x):
    return x

f = fun(2)

# f = ctypes.py_object(f)
print(f)
