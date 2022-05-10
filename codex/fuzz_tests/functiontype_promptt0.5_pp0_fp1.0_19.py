import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
assert not isinstance(func, types.BuiltinFunctionType)
assert not isinstance(func, types.MethodType)
assert not isinstance(func, types.BuiltinMethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)
# Test types.MethodType
class A:
    def f(self):
        pass
assert isinstance(A().f, types.MethodType)
assert not isinstance(A().f, types.FunctionType)
assert not isinstance(A().f, types.BuiltinFunctionType)
assert not isinstance(A().f, types.BuiltinMethodType)
# Test types.BuiltinMethodType
assert isinstance(str.upper, types.BuiltinMethodType)
assert not isinstance(str.upper, types.FunctionType)
assert
