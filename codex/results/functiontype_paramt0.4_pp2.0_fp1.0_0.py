from types import FunctionType
list(FunctionType(m.__code__, globals(), 'm'))

# %%
def m():
    for i in range(10):
        yield i

# %%
m.__code__

# %%
m.__code__.co_varnames

# %%
m.__code__.co_argcount

# %%
m.__code__.co_code

# %%
import dis
dis.dis(m)

# %%
def m(a, b):
    return a + b

# %%
m.__code__.co_varnames

# %%
m.__code__.co_argcount

# %%
dis.dis(m)

# %%
def m(a, b):
    c = a + b
    return c

# %%
dis.dis(m)

# %%
m.__code__.co_varnames

# %%
m.__code__.co_argcount

# %%
m.__code__.co_nlocals

# %%
m.__code__.
