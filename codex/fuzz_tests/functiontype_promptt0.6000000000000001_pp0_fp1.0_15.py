import types
# Test types.FunctionType
def f1(): pass
def f2(a): pass
def f3(a, *b, **c): pass
def f4(a, *b, c=0, **d): pass
def f5(a, b=0, c=1): pass
def f6(a, b=0, c=1, *d, **e): pass
def f7(a, b, c=0, *d, **e): pass
def f8(a, b=0, c=1, *d, e, **f): pass
def f9(a, b, c=0, *d, e, **f): pass
def f10(*a): pass
def f11(**a): pass
def f12(*a, **b): pass
def f13(a, *b, **c, **d): pass
def f14(a, *b, c, **d): pass
def f15(a, *b, c=0, **d): pass
def f16(a, *b, c=0, d=1, **e): pass
def f17
