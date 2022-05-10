import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print(a, b)
    return a + b

CMPFUNC = FUNTYPE(func)
print(CMPFUNC(1, 2))
</code>
Output:
<code>1 2
3
</code>

