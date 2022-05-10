import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun.__name__ = 'fun'

def fun_wrapper(f):
    def wrapper(*args, **kwargs):
        return f()
    return wrapper

fun = fun_wrapper(fun)
