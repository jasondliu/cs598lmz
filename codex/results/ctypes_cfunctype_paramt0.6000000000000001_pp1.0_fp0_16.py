import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_fun(x, y):
    return x + y

c_fun = FUNTYPE(py_fun)

print c_fun(1, 2)
</code>
I am using Python 2.7.4, Windows 7, and PyDev 2.8.2.0.

