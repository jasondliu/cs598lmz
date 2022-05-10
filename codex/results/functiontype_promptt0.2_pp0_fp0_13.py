import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)
assert not isinstance(a.f, types.FunctionType)
assert not isinstance(a.f, types.BuiltinFunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)
assert not isinstance(l, types.BuiltinFunctionType)
assert not isinstance(l, types.MethodType)

# Test types.GeneratorType

