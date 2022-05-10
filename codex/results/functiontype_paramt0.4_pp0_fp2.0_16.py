from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# %%
def f(a, b, c):
    pass

list(f.__code__.co_varnames)

# %%
def f(a, b, c, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

# %%
def f(a, b, c, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

# %%
def f(a, b, c, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

# %%
def f(a, b, c, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

# %%
def f(a, b, c, *args, **kwargs):
    pass

list(f.__code__.co_varnames)

# %%
def
