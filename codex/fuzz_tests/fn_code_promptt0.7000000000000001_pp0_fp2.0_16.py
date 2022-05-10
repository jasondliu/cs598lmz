fn = lambda: None
# Test fn.__code__.__str__() in a few scenarios.

def f1(a, b, c):
    pass

def f2(a, b=1, c=2):
    pass

def f3(a, b, c, *args):
    pass

def f4(a, b, c, **kwargs):
    pass

def f5(a, b, c, *args, **kwargs):
    pass

def f6(a, b, c, *, d, e):
    pass

def f7(a, b, c, *, d=1, e=2):
    pass

def f8(a, b=1, c=2, *, d, e):
    pass

def f9(a, b=1, c=2, *, d=1, e=2):
    pass

def f10(a, b, c, *args, d, e, **kwargs):
    pass

def f11(a, b, c, *args, d=1, e=2, **kwargs
