import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
assert type(f) != types.MethodType

class C:
    def f(self): pass
    def g(self): pass

assert type(C.f) == types.MethodType
assert type(C.g) == types.MethodType
assert type(C.f) != types.FunctionType
assert type(C.g) != types.FunctionType
c = C()
assert type(c.f) == types.MethodType
assert type(c.g) == types.MethodType
assert type(c.f) != types.FunctionType
assert type(c.g) != types.FunctionType

class D(C):
    pass

d = D()
assert type(d.f) == types.MethodType
assert type(d.g) == types.MethodType
assert type(d.f) != types.FunctionType
assert type(d.g) != types.FunctionType

class E:
    def f(self): pass
    def
