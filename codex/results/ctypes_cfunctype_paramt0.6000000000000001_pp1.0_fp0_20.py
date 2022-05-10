import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def bar(x):
    return 2*x

def foo(fn):
    return fn(1)

c_bar = FUNTYPE(bar)

print foo(c_bar)
</code>

