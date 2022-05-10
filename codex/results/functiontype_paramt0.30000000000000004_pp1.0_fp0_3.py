from types import FunctionType
list(FunctionType(lambda x: x + 1, {}, '', (), None, None, '').__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f.__code__.co_varnames)

#%%
def f(x, y):
    return x + y

list(f
