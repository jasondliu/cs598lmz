import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.c_double)


def py_fun(x, y):
    print(x, y)


fun_ptr = FUNTYPE(py_fun)
c_fun(fun_ptr)
</code>

