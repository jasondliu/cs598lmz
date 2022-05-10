import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('Hello')
    return 4

def fun1(f):
    print(f())

fun1(fun)
