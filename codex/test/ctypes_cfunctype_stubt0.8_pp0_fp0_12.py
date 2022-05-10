import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

def func_wrapper(func, **kw):
    return fun()

func_wrapper(lambda x: x, foo='bar')
