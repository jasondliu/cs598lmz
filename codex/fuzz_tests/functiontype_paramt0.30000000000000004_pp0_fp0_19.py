from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# %%
# Example 3
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
# Example 4
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
# Example 5
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
# Example 6
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
# Example 7
def f(x, y, z):
    return x + y + z

list(f.__code__.co_varnames)

# %%
# Example 8
def f(x, y, z):
    return x + y + z

list(f
