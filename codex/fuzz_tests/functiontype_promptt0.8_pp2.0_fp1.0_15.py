import types
# Test types.FunctionType

def f1(a, b, c):
    pass

def f2(a, b, c, e=None, f=[], g=1.1, h=None, i=-1, j=(), k={}):
    pass

assert type(f1) == types.FunctionType
assert type(f2) == types.FunctionType

assert isinstance(f1, types.FunctionType)
assert isinstance(f2, types.FunctionType)
print('function __defaults__')

def f1(a, b=1, c=2):
    return a, b, c

f2 = lambda a, b, c=3: (a, b, c)

assert f1.__defaults__ == (1, 2)
assert f2.__defaults__ == (3,)

def f3(a, b, c, *d, e=4, f, g=5, **kw):
    return a, b, c, d, e, f, g, kw

assert f3.__defaults__ == (4, 5
