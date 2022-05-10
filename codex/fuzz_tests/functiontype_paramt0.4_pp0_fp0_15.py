from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f').__globals__.keys())

# %%
def f(x):
    return x + 1

f.__closure__

# %%
def f(x, y, z):
    return x + y + z

f.__code__.co_varnames

# %%
def f(x, y, z):
    return x + y + z

f.__code__.co_varnames[:f.__code__.co_argcount]

# %%
def f(x, y, z):
    return x + y + z

f.__code__.co_varnames[f.__code__.co_argcount:]

# %%
def f(x, y, z):
    return x + y + z

f.__code__.co_varnames[:f.__code__.co_argcount]

# %%
def f(x, y, z):
    return x + y + z

f.__code__.co_varn
