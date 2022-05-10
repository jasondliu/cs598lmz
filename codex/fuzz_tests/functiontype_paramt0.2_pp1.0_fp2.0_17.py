from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# %%
import inspect
def f():
    a = 1
    b = 2
    c = 3
    return a + b + c

inspect.getargspec(f)

# %%
import inspect
def f(a, b, c=3, *args, **kwargs):
    return a + b + c

inspect.getargspec(f)

# %%
import inspect
def f(a, b, c=3, *args, **kwargs):
    return a + b + c

inspect.getargspec(f).args

# %%
import inspect
def f(a, b, c=3, *args, **kwargs):
    return a + b + c

inspect.getargspec(f).varargs

# %%
import inspect
def f(a, b, c=3, *args, **kwargs):
    return a + b + c

inspect.getargspec(f).keywords

# %%
import inspect
def
