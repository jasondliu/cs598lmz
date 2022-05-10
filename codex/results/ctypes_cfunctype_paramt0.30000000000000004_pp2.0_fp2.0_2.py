import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def foo(x):
    print("foo called with", x)
    return 42

c_foo = FUNTYPE(foo)
c_foo(5)
</code>

