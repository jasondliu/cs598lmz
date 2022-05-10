import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def f(x):
    return math.cos(x)

my_func = FUNTYPE(f)
print(my_func(4))
</code>
The following code does not work.
<code>import ctypes
import math
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def f(x):
    return math.cos(x)

my_func = FUNTYPE(f)
print(my_func(4))
</code>
Why is this?


A:

The reason is that <code>math.cos</code> is a Python object, and the <code>CFUNCTYPE</code> machinery won't work with it. You can't use <code>CFUNCTYPE</code> to wrap arbitrary Python functions.
You have to use a function implemented in C.

