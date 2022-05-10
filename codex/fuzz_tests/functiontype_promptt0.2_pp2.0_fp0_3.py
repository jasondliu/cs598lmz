import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.LambdaType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert isinstance(A().f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance
