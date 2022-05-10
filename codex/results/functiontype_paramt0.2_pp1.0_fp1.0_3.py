from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

#%%
def f(x):
    return x

f.__code__.co_varnames

#%%
def f(x):
    return x

f.__code__.co_argcount

#%%
def f(x):
    return x

f.__code__.co_nlocals

#%%
def f(x):
    return x

f.__code__.co_stacksize

#%%
def f(x):
    return x

f.__code__.co_flags

#%%
def f(x):
    return x

f.__code__.co_consts

#%%
def f(x):
    return x

f.__code__.co_names

#%%
def f(x):
    return x

f.__code__.co_varnames

#%%
