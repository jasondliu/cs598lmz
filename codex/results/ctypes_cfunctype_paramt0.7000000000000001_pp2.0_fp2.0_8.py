import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def wrapper(func, argtypes, restype=ctypes.c_int):
    cfunc = FUNTYPE(func)
    cfunc.argtypes = argtypes
    cfunc.restype = restype
    return cfunc

f1 = wrapper(myfunc, [ctypes.c_int])
f2 = wrapper(myfunc, [ctypes.c_int], ctypes.c_void_p)

print f1(5)
print f2(5)
</code>
output:
<code>10
0x3e8
</code>

