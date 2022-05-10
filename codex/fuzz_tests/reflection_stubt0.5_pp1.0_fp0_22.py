fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

#------------------------------------------------------------------------
# Test __code__ on various objects that are not callable

# test on functions
def f1():
    pass

def f2(x):
    pass

def f3(x, y):
    pass

def f4(x, y, z):
    pass

def f5(x, y, z, w):
    pass

def f6(x, y, z, w, v):
    pass

def f7(x, y, z, w, v, u):
    pass

def f8(x, y, z, w, v, u, t):
    pass

def f9(x, y, z, w, v, u, t, s):
    pass

def f10(x, y, z, w, v, u, t, s, r):
    pass

def f11(x, y, z, w, v, u, t, s, r, q):
    pass

def f12(x, y, z, w, v, u
