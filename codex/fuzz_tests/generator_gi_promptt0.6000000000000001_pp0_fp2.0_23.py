gi = (i for i in ())
# Test gi.gi_code.co_firstlineno == 0

# An empty function.
def f(): pass
def g(x): pass
def h(x, y, z): pass
def i(x, y, z, w): pass
def j(x, y, z, w, u): pass
def k(x, y, z, w, u, v, **kwargs): pass
def l(x, y, z, w, u, v, *args): pass
def m(x, y, z, w, u, v, *args, **kwargs): pass
def n(x, y, z, w, u, v, *args, **kwargs): pass
def o(x, y, z, w, u, v, *, kwonly=True): pass
def p(x, y, z, w, u, v, *args, kwonly=True): pass
def q(x, y, z, w, u, v, *args, kwonly=True, **kwargs): pass
def r(x, y, z, w, u, v, *, k
