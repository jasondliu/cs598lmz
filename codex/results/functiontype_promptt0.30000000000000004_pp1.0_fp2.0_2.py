import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
assert not isinstance(func, types.BuiltinFunctionType)
assert not isinstance(func, types.MethodType)
assert not isinstance(func, types.BuiltinMethodType)
assert not isinstance(func, types.LambdaType)
assert not isinstance(func, types.GeneratorType)
assert not isinstance(func, types.CodeType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.LambdaType)
assert not isinstance(len, types.GeneratorType)
assert not isinstance(len, types.CodeType)
# Test types.MethodType
class A:
    def method(self):
        return self
a = A()
assert isinstance(a.method, types.MethodType)

