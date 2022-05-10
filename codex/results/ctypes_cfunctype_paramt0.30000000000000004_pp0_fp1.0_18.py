import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)

print(cfunc(1, 2))
</code>
This works fine, but I want to be able to pass a function that takes a variable number of arguments. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, *(ctypes.c_int,)*10)

def func(*args):
    return sum(args)

cfunc = FUNTYPE(func)

print(cfunc(1, 2))
</code>
But this fails with:
<code>TypeError: expected LP_CFUNCTYPE instance, got int
</code>
I also tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, *(ctypes.c_int,)*10)

def func(*args):
    return sum(args)

