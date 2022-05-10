import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello from ctypes")
    return "Test"
libfun = ctypes.cdll.LoadLibrary("./libfun.so")
libfun.fun.restype = ctypes.py_object
libfun.fun.argtypes = [FUNTYPE]
res = libfun.fun(fun)
print("Result:", res)
</code>

