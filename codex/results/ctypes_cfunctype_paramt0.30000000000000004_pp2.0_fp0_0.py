import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def foo(a, b):
    print a, b
    return a + b

f = FUNTYPE(foo)
print f(1, 2)
</code>
The output is:
<code>1 2
3
</code>

