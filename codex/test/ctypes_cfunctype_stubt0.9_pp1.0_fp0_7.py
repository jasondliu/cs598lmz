import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world!"
fun()

type(ctypes.c_int)
# Add two numbers using ctypes
a = 7
b = 5

