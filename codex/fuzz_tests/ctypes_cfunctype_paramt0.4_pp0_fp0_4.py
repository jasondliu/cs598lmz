import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def do_something(value):
    return value + 1

my_func = FUNTYPE(do_something)
print my_func(2)

</code>

