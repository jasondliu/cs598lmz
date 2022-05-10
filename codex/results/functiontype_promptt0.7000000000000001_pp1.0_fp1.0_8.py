import types
# Test types.FunctionType(code, globals, name, argdefs, closure)
def f():
    pass

def f(x):
    pass

def f(x, y):
    pass

def f(x, y, *z):
    pass

def f(x, y, **z):
    pass

def f(x, y, *z, **u):
    pass

def f(x, y, *, u, **v):
    pass

def f(x, y=2):
    pass

def f(x, y=2, *z):
    pass

def f(x, y=2, **z):
    pass

def f(x, y=2, *z, **u):
    pass

def f(x, y=2, *, u, **v):
    pass

def f(x, *z):
    pass

def f(x, *z, **u):
    pass

def f(x=1):
    pass

def f(x=1, y=2):
   
