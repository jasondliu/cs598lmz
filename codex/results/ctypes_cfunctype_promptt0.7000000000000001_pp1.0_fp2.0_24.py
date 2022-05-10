import ctypes
# Test ctypes.CFUNCTYPE
py_inspect = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(inspect.__dict__['getargspec'])
py_inspect(5)

py_inspect = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(inspect.getargspec)
py_inspect(5)

py_inspect = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(inspect.getargspec)
py_inspect(5)

py_inspect = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(inspect.getargspec)
py_inspect(5)

def func(arg):
    return arg

py_inspect = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
py_inspect(5)

py_inspect = ctypes.CFUNCTYPE(ctypes.c
