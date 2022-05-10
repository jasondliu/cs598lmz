from types import FunctionType
list(FunctionType(add.__code__, globals(), "add").__closure__)

#%%
def fn(x):
    def adder(y):
        return x + y
    return adder
fn(1).__closure__
#%%
def fn(x, y):
    def adder(z):
        return x + y + z
    return adder
fn(1, 2).__closure__
#%%
from types import FunctionType
def add(x):
    def adder(y):
        return x + y
    return adder
f = add(1)
f.__closure__

#%%
from types import FunctionType
def add(x):
    def adder(y):
        return x + y
    return adder
f = add(1)
list(FunctionType(f.__code__, globals(), "adder").__closure__)

#%%
from types import FunctionType
def add(x):
    def adder(y):
        return x + y
    return adder
f = add(1)
list(FunctionType(f
