from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# %%
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

f.__code__.co_varnames

# %%
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

f.__code__.co_varnames

# %%
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

f.__code__.co_varnames

# %%
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

f.__code__.co_varnames

# %%
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

f.__code__.co_varnames

# %%
def f():
    a = 1
    b = 2

