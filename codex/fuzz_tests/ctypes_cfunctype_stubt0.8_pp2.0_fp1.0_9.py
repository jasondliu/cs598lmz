import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    def f(x):
        return x**2
    return f
print(fun()(2)) # 4
