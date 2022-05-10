import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.BuiltinMethodType)
assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.LambdaType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert isinstance(l, types.FunctionType)
assert isinstance(l, types.BuiltinFunctionType)
assert isinstance(l, types.BuiltinMethodType)
assert not isinstance(l, types.MethodType)

# Test
