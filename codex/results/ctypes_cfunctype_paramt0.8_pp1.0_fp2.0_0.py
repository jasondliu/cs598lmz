import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int,ctypes.c_int)

def func(x, y):
    return x-y

C_FUNC = FUNTYPE(func)

@jit(nopython=True)
def function(x, y):
    return C_FUNC(x-y)

function(1, 1)
</code>
Or I am doing something wrong?


A:

<code>numba</code> doesn't allow you to pass <code>C_FUNC</code> to <code>@jit</code> decorated function. 
Here is a minimal example that demonstrates the problem:
<code>import ctypes
import numpy as np
from numba import jit

@jit(nopython=True)
def f(x):
    return x + 1.0

def wrap_f(x):
    return f(x)

def wrap_f_ctype(x):
    f1 = f.ctypes
    return f1(x)

def wrap_f_callable(x
