import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object("hello world")
x = fun()
print(x) # hello world
</code>

