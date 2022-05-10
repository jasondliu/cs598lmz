import types
# Test types.FunctionType

def f(): pass

def g(x): pass

def h(*args): pass

def i(**kw): pass

def j(x, *args, **kw): pass

def k(x=None): pass

def l(x=None, *args, **kw): pass

def m(x, y=None, *args, **kw): pass

def n(x, y=1, *args, **kw): pass

def o(x, y=1, *args, z=2, **kw): pass

def p(x, y=1, *args, z=2, **kw): pass

def q(x, y=1, *, z=2, **kw): pass

def r(x, y=1, *, z=2, **kw): pass

def s(x, y=1, *, z=2, **kw): pass

def t(x, y=1, *, z=2, **kw): pass

def u(x, y=1, *, z=2, **kw):
