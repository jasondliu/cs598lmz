import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

#define the callback function
def py_func(a, b):
    print("{} + {} = {}".format(a, b, a + b))
    return a + b

#convert the python function into a c callback function
c_func = FUNTYPE(py_func)

#call the c function, which will call the python function
c_add(2, 3, c_func)
</code>

