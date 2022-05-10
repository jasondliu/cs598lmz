import types
# Test types.FunctionType

def f(): pass

def f2(a): pass

def f3(a, b): pass

def f4(a, b=1): pass

def f5(a=1, b=2): pass

def f6(a=1, *args): pass

def f7(*args): pass

def f8(a, *args): pass

def f9(**args): pass

def f10(a, **args): pass

def f11(a, *args, **kw): pass

def f12(a, b=2, *args, **kw): pass

def f13(a, b=2, *, c, **kw): pass

def f14(a, b=2, *, c=3, **kw): pass

def f15(a, b=2, *args, c=3, **kw): pass

def f16(a, b=2, *, c=3, d=4, **kw): pass

def f17(a, b=2, *, c=3, d
