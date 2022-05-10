import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

def f2():
    fun()

f2()
f2()

f()
f()
