from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

#%%
def f(x):
    def g(y):
        return x + y
    return g

f(1)(2)

#%%
def f(x):
    def g(y):
        return x + y
    return g

f(1).__code__ is f(2).__code__

#%%
def f(x):
    def g(y):
        return x + y
    return g

f(1).__closure__

#%%
def f(x):
    def g(y):
        return x + y
    return g

f(1).__closure__[0].cell_contents

#%%
def f(x):
    def g(y):
        return x + y
    return g

f(1).__closure__[0].cell_contents = 3
f(1)(2)

#%%
