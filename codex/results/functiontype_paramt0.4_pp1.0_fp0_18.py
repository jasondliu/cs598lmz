from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

#%%
def f(x, y, z):
    pass

list(f.__code__.co_varnames)

#%%
def f(x, y, z, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

#%%
def f(x, y, z, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

#%%
def f(x, y, z, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

#%%
def f(x, y, z, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

#%%
def f(x, y, z, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

#%%
def
