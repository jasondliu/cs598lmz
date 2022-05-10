import ctypes
# Test ctypes.CFUNCTYPE()
def func(x,y):
    return x+y

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
f(2,3)

# Test ctypes.pythonapi
ctypes.pythonapi.Py_GetVersion()

# Test ctypes.pydll
