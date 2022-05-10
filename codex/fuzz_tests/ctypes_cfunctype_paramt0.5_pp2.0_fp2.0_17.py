import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.c_int )

def my_callback(a,b):
    print 'got:', a, b
    return a+b

callback = FUNTYPE(my_callback)

mydll = ctypes.CDLL('mydll.dll')
mydll.my_function.argtypes = [FUNTYPE, ctypes.c_int]
mydll.my_function.restype = ctypes.c_int

result = mydll.my_function(callback, 4)
print 'done:', result
</code>

