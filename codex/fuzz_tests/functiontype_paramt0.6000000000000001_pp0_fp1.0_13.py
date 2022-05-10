from types import FunctionType
list(FunctionType(h,globals(),'f'))

# or

h = lambda x:[x-1,x,x+1]
f = FunctionType(h.__code__,h.__globals__,h.__name__,h.__defaults__,h.__closure__)
list(f(3))

# or

import types
h = lambda x:[x-1,x,x+1]
f = types.FunctionType(h.__code__,h.__globals__,h.__name__,h.__defaults__,h.__closure__)
list(f(3))

# or

import functools
h = lambda x:[x-1,x,x+1]
f = functools.partial(h, None)
list(f(3))

# or

def h(x):
    return [x-1,x,x+1]
f = h
list(f(3))

# or

import functools
h = lambda x:[x-1,x,x+
