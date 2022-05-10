from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
def f(x, y
