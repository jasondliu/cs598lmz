from types import FunctionType
list(FunctionType(f.__code__,globals(),name="sub"))()

#%%
from types import FunctionType
f = lambda x,y:x+y
g = FunctionType(f.__code__,globals(),name="sub")
g(1,2)

#%%
def f(a,b):
    return a+b
f.__code__ = (lambda x,y:x-y).__code__
f(1,2)

#%%
def f(a,b):
    return a+b
f.__code__ = (lambda x,y:x-y).__code__
f.__defaults__ = (1,2)
f()

#%%
def f(a,b):
    return a+b
f.__code__ = (lambda x,y:x-y).__code__
f.__defaults__ = (1,2)
f.__globals__["print"] = lambda *a,**b:None
f()

#%%
def f(a,b):
    return a+b

