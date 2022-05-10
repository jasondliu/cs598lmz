import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@jit(nopython=True)
def f(x):
    return x

f(fun())
</code>

