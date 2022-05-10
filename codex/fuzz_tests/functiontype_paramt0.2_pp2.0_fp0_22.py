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
inspect.getargvalues(f)

#%%
def f(a, b, c):
    pass
inspect.getcallargs(f, 1, 2, 3)

#%%
def f(a, b, c):
    pass
inspect.getclosurevars(f)

#%%
def f(a, b, c):
    pass
inspect.getgeneratorlocals(f)

#%%
def f(a, b, c):
    pass
inspect.getgeneratorstate(f)

#%%
def f(a, b, c):
    pass
inspect.getouterframes(f)

#%%
def f(a
