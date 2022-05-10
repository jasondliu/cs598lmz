import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print(a, b)
    return a + b

my_callback_type = FUNTYPE(my_callback)

mydll = ctypes.CDLL("mydll")
mydll.myfunc.argtypes = (ctypes.c_int, ctypes.c_int, my_callback_type)
mydll.myfunc.restype = ctypes.c_int

print(mydll.myfunc(1, 2, my_callback_type))
</code>

