from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

#%%
def f(a, b, c):
    return a + b + c
list(f.__code__.co_varnames)

#%%
def f(a, b, c, d):
    return a + b + c + d
list(f.__code__.co_varnames)

#%%
def f(a, b, c, d, e):
    return a + b + c + d + e
list(f.__code__.co_varnames)

#%%
def f(a, b, c, d, e, f):
    return a + b + c + d + e + f
list(f.__code__.co_varnames)

#%%
def f(a, b, c, d, e, f, g):
    return a + b + c + d + e + f + g
list(f.__code__.co_varnames)

#%%
def f(a, b, c,
