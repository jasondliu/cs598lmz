import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(3, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert not isinstance(isinstance, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(func, types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(3)), types.GeneratorType)
assert not isinstance((x for x in range(3)).__next__, types.GeneratorType)

# Test types.MethodType
class A(object):
    def foo(self):
        pass
assert isinstance(A().foo, types.MethodType)
assert not isinstance(A.foo, types.MethodType)

# Test types.
