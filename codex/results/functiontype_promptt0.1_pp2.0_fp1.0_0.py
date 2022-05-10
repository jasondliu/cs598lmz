import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert not isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class D:
    def f(self): pass
assert isinstance(D().f, types.MethodType)
assert isinstance(D().f, types.BuiltinMethodType)
assert not isinstance(D().f, types.FunctionType)
assert not isinstance(D().f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance
