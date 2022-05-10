import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world!"

def fun_wrapper(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs)
    return wrapper
