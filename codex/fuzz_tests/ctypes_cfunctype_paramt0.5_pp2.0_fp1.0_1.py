import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

# convert func to a c function
f = FUNTYPE(func)

# use the c function
print(f(2))

# convert back to a python function
g = f.__wrapped__
print(g(2))
</code>
Output:
<code>4.0
4.0
</code>

