import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    return x + 1

c_func = FUNTYPE(py_func)

print "py_func(1) =", py_func(1)
print "c_func(1) =", c_func(1)
