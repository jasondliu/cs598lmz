fn = lambda: None
# Test fn.__code__.co_argcount

def f0(): pass
def f1(a): pass
def f2(a, b): pass
def f3(a, b, c): pass
def f4(a, b, c, d): pass
def f5(a, b, c, d, e): pass
def f6(a, b, c, d, e, f): pass
def f7(a, b, c, d, e, f, g): pass

def f8(*a): pass
def f9(**a): pass
def f10(*a, **b): pass
def f11(a, *b): pass
def f12(a, **b): pass
def f13(a, b, *c): pass
def f14(a, b, **c): pass
def f15(a, b, c, *d): pass
def f16(a, b, c, **d): pass
def f17(a, b, c, d, *e): pass
def f18(a, b, c, d, **e): pass
def f19
