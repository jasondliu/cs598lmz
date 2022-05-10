import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print("hello from myfunc", n)
    return n + 1

f = FUNTYPE(myfunc)

f(42)
print(f(42))
print(f(1))
print(f(99))
</code>

