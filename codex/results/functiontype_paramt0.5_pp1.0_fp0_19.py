from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

#%%
def f(a, b):
    def g(x):
        return x + a + b
    return g

#%%
def f(a, b):
    return lambda x: x + a + b

#%%
def f(a, b):
    return lambda x, a=a, b=b: x + a + b

#%%
def f(a, b):
    return lambda *args, a=a, b=b: sum(args) + a + b

#%%
def f(a, b):
    return lambda *args, a=a, b=b, **kwargs: (sum(args) + a + b, kwargs)

#%%
def f(a, b):
    return lambda *args, a=a, b=b, **kwargs: (sum(args) + a + b, kwargs)

#%%
