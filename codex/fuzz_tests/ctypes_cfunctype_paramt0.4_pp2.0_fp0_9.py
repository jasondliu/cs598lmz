import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print('myfunc(%d, %d)' % (a, b))
    return a + b

func = FUNTYPE(myfunc)

print(func(1, 2))
</code>

