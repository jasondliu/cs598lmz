import types
# Test types.FunctionType and types.LambdaType
def f():
    pass
def f2(a):
    return a
def f3(a, b):
    return a + b
def f4(*args):
    return len(args)
def f5(x, y, z=3, *args):
    return x + y + z + len(args)
def f6(x, y, z=3, *args, **kw):
    return x + y + z + len(args) + len(kw)
def f7(x, y, z=3, *, a, b=4):
    return x + y + z + a + b
def f8(x, y, z=3, *, a, b=4, **kw):
    return x + y + z + a + b + len(kw)
def f9(x, y, z=3, *, a, b=4, **kw):
    m = x + y + z + a + b + len(kw)
    def f10():
        return m
    f10.x = 1

