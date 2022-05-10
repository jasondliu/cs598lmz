from types import FunctionType
list(FunctionType(lambda :None,globals()).__code__.co_varnames)

# %%
def f(a,b,c):
    d = a + b + c
    e = a * b * c
    return d, e
list(FunctionType(f.__code__,globals()).__code__.co_varnames)

# %%
def f(a:int,b:int,c:int) -> tuple:
    d = a + b + c
    e = a * b * c
    return d, e
list(FunctionType(f.__code__,globals()).__code__.co_varnames)

# %%
def f(a:int,b:int,c:int) -> tuple:
    d = a + b + c
    e = a * b * c
    return d, e
FunctionType(f.__code__,globals()).__annotations__

# %%
def f(a:int,b:int,c:int) -> tuple:
    d = a + b +
