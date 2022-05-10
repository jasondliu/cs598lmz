from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# %%
from types import FunctionType
def f(): pass
list(FunctionType(f.__code__, {}).__code__.co_varnames)

# %%
from types import FunctionType
def f(x): pass
list(FunctionType(f.__code__, {}).__code__.co_varnames)

# %%
from types import FunctionType
def f(x, y=1): pass
list(FunctionType(f.__code__, {}).__code__.co_varnames)

# %%
from types import FunctionType
def f(x, y=1, *args): pass
list(FunctionType(f.__code__, {}).__code__.co_varnames)

# %%
from types import FunctionType
def f(x, y=1, *args, z=2, **kwargs): pass
list(FunctionType(f.__code__, {}).__code__.co_varnames)

# %%
from types import FunctionType
