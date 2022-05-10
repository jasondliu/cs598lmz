import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)
assert not isinstance(l, types.BuiltinFunctionType)

# Test types.GeneratorType
g = (i for i in range(10))
assert isinstance(g, types.GeneratorType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types
