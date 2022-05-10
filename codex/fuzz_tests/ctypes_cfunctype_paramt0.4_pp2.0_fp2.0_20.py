import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print('hello world', a, b)

func_ptr = FUNTYPE(func)

libc.my_func(func_ptr)
</code>

