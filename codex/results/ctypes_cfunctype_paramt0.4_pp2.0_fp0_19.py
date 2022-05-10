import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def get_fun(fn):
    return FUNTYPE(fn)

def f(x):
    return x + 1

f2 = get_fun(f)

print f2(2)

# This is the same as the previous example, but now we use a decorator
# to automatically convert the function to a CFUNCTYPE.

def callback(fn):
    return FUNTYPE(fn)

@callback
def f(x):
    return x + 1

print f(2)
</code>

