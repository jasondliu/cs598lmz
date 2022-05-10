import types
types.FunctionType(lambda: None)

#%%
import types
def f():
    pass
f1 = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)
f1()

#%%
import types
def f():
    pass
f1 = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)
f1()

#%%
import types
def f():
    pass
f1 = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)
f1()

#%%
import types
def f():
    pass
