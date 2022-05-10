import types
# Test types.FunctionType and types.LambdaType

# types.FunctionType(code, globals, name, argdefs, closure)
def f(x):
    pass

def g(x):
    return x

def h(x, y, z):
    return x+y+z

def i(x, y, z=1, *w):
    return x+y+z+len(w)

def j(x, y, z=1, *w, **k):
    return x+y+z+len(w)+len(k)

def k(x, y, z=1, *w, **k):
    return x+y+z+len(w)+len(k)

def l(x, y, z=1, *w, **k):
    return x+y+z+len(w)+len(k)

def m(x, y, z=1, *w, **k):
    return x+y+z+len(w)+len(k)

def n(x, y, z=1, *w
