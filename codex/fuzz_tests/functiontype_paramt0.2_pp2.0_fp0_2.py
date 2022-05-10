from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# %%
def f(a, b, c):
    return a + b + c

list(f.__code__.co_varnames)

# %%
def f(a, b, c):
    return a + b + c

f.__code__.co_varnames

# %%
def f(a, b, c):
    return a + b + c

f.__code__.co_varnames

# %%
def f(a, b, c):
    return a + b + c

f.__code__.co_varnames

# %%
def f(a, b, c):
    return a + b + c

f.__code__.co_varnames

# %%
def f(a, b, c):
    return a + b + c

f.__code__.co_varnames

# %%
def f(a, b, c):
    return a + b + c

f.
