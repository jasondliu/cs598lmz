from types import FunctionType
list(FunctionType(lambda:None,{}).__code__.co_varnames)

#%%
def f(x):
    a = 1
    b = 2
    c = 3
    return a + b + c

list(f.__code__.co_varnames)

#%%
def f(x):
    a = 1
    b = 2
    c = 3
    return a + b + c

list(f.__code__.co_varnames)

#%%
def f(x):
    a = 1
    b = 2
    c = 3
    return a + b + c

list(f.__code__.co_varnames)

#%%
def f(x):
    a = 1
    b = 2
    c = 3
    return a + b + c

list(f.__code__.co_varnames)

#%%
def f(x):
    a = 1
    b = 2
    c = 3
    return a + b + c

list(f.__code__
