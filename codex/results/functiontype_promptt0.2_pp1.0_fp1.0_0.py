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
assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.BuiltinFunctionType)
assert isinstance(C.f, types.BuiltinMethodType)
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.LambdaType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.FunctionType)
assert isinstance(g, types.BuiltinFunctionType)
assert isinstance(g, types.BuiltinMethodType)
assert isinstance(g, types.MethodType)
assert isinstance(g, types.LambdaType)

# Test types.
