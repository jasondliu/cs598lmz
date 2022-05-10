import types
# Test types.FunctionType
def f(x):
    return x

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.MethodType
class A(object):
    def f(self, x):
        return x

a = A()
assert isinstance(a.f, types.MethodType)
assert not isinstance(a.f, types.FunctionType)
assert not isinstance(a.f, types.BuiltinFunctionType)
assert not isinstance(a.f, types.BuiltinMethodType)
assert not isinstance(a.f, types.LambdaType)

# Test types.LambdaType
l = lambda x: x
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)
assert not isinstance(l, types.BuiltinFunctionType)
assert not
