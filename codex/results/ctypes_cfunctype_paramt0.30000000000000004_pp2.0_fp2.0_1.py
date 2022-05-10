import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print('my_callback called with %d and %d' % (a, b))
    return a + b

my_callback = FUNTYPE(my_callback)

mydll = ctypes.CDLL('mydll.dll')
mydll.set_callback(my_callback)

print('3 + 5 =', mydll.add_with_callback(3, 5))
</code>

