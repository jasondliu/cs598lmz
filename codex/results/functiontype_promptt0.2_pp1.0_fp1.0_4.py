import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.LambdaType)
assert not isinstance(len, types.GeneratorType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C().f, types.MethodType)
assert not isinstance(C().f, types.FunctionType)
assert not isinstance(C().f, types.BuiltinFunctionType)
assert not isinstance(
