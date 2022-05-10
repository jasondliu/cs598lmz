from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# %%
from types import FunctionType
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)

# %%
from types import FunctionType
f = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
f(1, 2)

# %%
from types import FunctionType
def f(a, b):
    return a + b

def g(a, b):
    return a * b

def h(a, b):
    return a - b

def apply_func(func, a, b):
    return func(a, b)

apply_func(f, 2, 3)

# %%
from types import FunctionType
def f(a, b):
    return a + b

def g(a,
