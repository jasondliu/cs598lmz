import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print("hello from myfunc", n)
    return n * 2

f = FUNTYPE(myfunc)
print(f(42))
</code>
The output is:
<code>hello from myfunc 42
84
</code>

