import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
F = FUNTYPE(lambda x: x*x)
print(F(4))

# Note that you cannot use decorators and @ to wrap the lambda
from ctypes import *
from functools import partial

@CFUNCTYPE(c_double, c_double)
def square_function(x):
    return x*x

print(square_function(4))
square_partial = partial(square_function, 4)
print(square_partial())
</code>

