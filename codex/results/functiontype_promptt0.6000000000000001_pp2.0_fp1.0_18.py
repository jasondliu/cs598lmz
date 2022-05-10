import types
# Test types.FunctionType, types.LambdaType, types.CodeType

def f():
    pass

def g():
    1 + 1

def h():
    return

def i():
    return 1

def j(x):
    return x

def k(x, y, z):
    return x + y + z

def l(x, y, z, *args):
    return x + y + z + len(args)

def m(x, y, z, *args, **kwargs):
    return x + y + z + len(args) + len(kwargs)

def n(x, y, z, m=None, n=None, *args, **kwargs):
    return x + y + z + m + n + len(args) + len(kwargs)

def o(x, y, z, m=None, n=None, *args, **kwargs):
    return x + y + z + m + n + len(args) + len(kwargs)

class A:
    def m1(self):
        pass
