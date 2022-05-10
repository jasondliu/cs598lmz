from types import FunctionType
list(FunctionType(lambda x:x,{}).__code__.co_varnames)

# %%
list(FunctionType(lambda x:x,{}).__code__.co_freevars)

# %%
list(FunctionType(lambda x:x,{}).__code__.co_cellvars)

# %%
def f(x):
    y = x
    def g(z):
        return y + z
    return g

# %%
list(f(1).__code__.co_varnames)

# %%
list(f(1).__code__.co_freevars)

# %%
list(f(1).__code__.co_cellvars)

# %%
def f(x):
    y = x
    def g(z):
        nonlocal y
        y += z
        return y
    return g

# %%
list(f(1).__code__.co_varnames)

# %%
list(f(1).__code__.co_freevars)

# %%
