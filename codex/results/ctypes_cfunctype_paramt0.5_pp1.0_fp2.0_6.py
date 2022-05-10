import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def function(a, b):
    return a + b

f = FUNTYPE(function)

print f(1, 2)
print f(1, 9)
</code>

