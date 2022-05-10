import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

def f(x):
    return x*x

def g(x):
    return x+1

def h(x):
    return x*2

def compose(f, g, h):
    return lambda x: f(g(h(x)))

compose(f, g, h)(2)

#%%

def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs, x)

compose(f, g, h)(2)

#%%

def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

compose(f, g, h)(2)

#%%

def compose(*funcs):
    return reduce(lambda f, g: lambda *a, **kw: f(g(*a, **kw)), funcs)

compose(f, g, h)(2)

#%%

def compose(*funcs):
   
