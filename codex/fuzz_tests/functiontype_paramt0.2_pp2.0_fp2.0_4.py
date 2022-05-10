from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

#%%
import inspect
def f(a, b, c):
    pass
inspect.getfullargspec(f)

#%%
def f(a, b, c):
    pass
inspect.getargspec(f)

#%%
def f(a, b, c):
    pass
inspect.signature(f)

#%%
def f(a, b, c):
    pass
inspect.signature(f).parameters

#%%
def f(a, b, c):
    pass
inspect.signature(f).parameters['a']

#%%
def f(a, b, c):
    pass
inspect.signature(f).parameters['a'].default

#%%
def f(a, b, c):
    pass
inspect.signature(f).parameters['a'].kind

#%%
def f(a, b, c):
    pass
inspect.signature(f).parameters['a
