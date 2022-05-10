import types
# Test types.FunctionType

def f():
    pass

assert type(f) == types.FunctionType
assert type(f) is types.FunctionType

try:
    types.FunctionType(1, 2, 3)
except TypeError:
    pass
else:
    raise Exception, "did not raise TypeError"

try:
    types.FunctionType(1, 2, 3, 4, 5, 6)
except TypeError:
    pass
else:
    raise Exception, "did not raise TypeError"

class A:
    pass

def g():
    pass

def h(a, b, c, d):
    pass

a = A()

a.f = types.FunctionType(g.func_code, g.func_globals, "f", g.func_defaults,
                          g.func_closure)

assert a.f() == None

a.h = types.FunctionType(h.func_code, h.func_globals, "h", h.func_defaults,
                          h.func_closure)

assert
