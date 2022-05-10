from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# %%
def f():
    a = 1
    b = 2
    return a + b
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# %%
def f():
    a = 1
    b = 2
    def f_inner():
        return a + b
    return f_inner
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# %%
def f():
    a = 1
    b = 2
    def f_inner():
        return a + b
    return f_inner
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# %%
def f
