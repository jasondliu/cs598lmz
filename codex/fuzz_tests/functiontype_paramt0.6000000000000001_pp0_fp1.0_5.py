from types import FunctionType
list(FunctionType(f).__code__.co_varnames)

#%%
f = lambda x, y: x + y
f(1, 2)

#%%
f = lambda x, y: x + y
f = lambda x, y=1: x + y
f(1)

#%%
f = lambda x, y: x + y
f.__name__

#%%
f = lambda x, y: x + y
f.__doc__

#%%
f = lambda x, y: x + y
f.__code__

#%%
f = lambda x, y: x + y
f.__code__.co_code

#%%
f = lambda x, y: x + y
f.__code__.co_varnames

#%%
f = lambda x, y: x + y
f.__code__.co_argcount

#%%
f = lambda x, y: x + y
f.__code__.co_flags

#%%
def f():
    pass

f.__closure__

#%%
