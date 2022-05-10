import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def m(self): pass
assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.BuiltinMethodType)
assert not isinstance(C.m, types.FunctionType)
assert not isinstance(C.m, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class C:
    def m(self): pass
c = C()
assert isinstance(c.m, types.BuiltinMethodType)
assert not isinstance(c.m, types.MethodType)
assert not isinstance(c.m, types.FunctionType)
assert not isinstance(c.m, types.BuiltinFunctionType)

# Test types.GeneratorType
def g():
    yield
assert isinstance(g(),
