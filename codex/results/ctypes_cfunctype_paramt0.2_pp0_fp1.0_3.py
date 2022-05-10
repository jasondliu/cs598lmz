import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print("hello from python", n)
    return n * 2

f = FUNTYPE(myfunc)

print(f(42))
</code>

