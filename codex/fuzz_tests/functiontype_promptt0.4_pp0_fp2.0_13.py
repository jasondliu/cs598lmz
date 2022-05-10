import types
# Test types.FunctionType
def f1(x):
    return x * 2

def f2(x, y):
    return x + y

def f3(x, y, z):
    return x + y + z

def f4(x, y, z=3):
    return x + y + z

def f5(x, y=2, z=3):
    return x + y + z

def f6(x, *args):
    return x + sum(args)

def f7(x, **kwargs):
    return x + sum(kwargs.values())

def f8(x, *args, **kwargs):
    return x + sum(args) + sum(kwargs.values())

def f9(x, y, *args, **kwargs):
    return x + y + sum(args) + sum(kwargs.values())

def f10(x, y=2, *args, **kwargs):
    return x + y + sum(args) + sum(kwargs.values())

def f11(x, y=
