from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "name", f.__defaults__, f.__closure__))

# %%
# f.__code__
# f.__globals__
# f.__defaults__
# f.__closure__

# %%
def f(a, b=1, *args, **kwargs):
    print(a, b, args, kwargs)

# %%
f.__code__

# %%
f.__code__.co_varnames

# %%
f.__code__.co_argcount

# %%
f.__code__.co_flags

# %%
f.__code__.co_code

# %%
f.__code__.co_consts

# %%
f.__code__.co_names

# %%
f.__code__.co_nlocals

# %%
f.__code__.co_stacksize

# %%
f.__code__.co_firstlineno

# %%
f.__code
