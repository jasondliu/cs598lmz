import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.BuiltinFunctionType)
assert not isinstance(A.f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert isinstance(l, types.FunctionType)
assert isinstance(l, types.BuiltinFunctionType)
assert not isinstance(l, types.BuiltinMethodType)
assert not isinstance(l, types.MethodType)

# Test types.GeneratorType
def g():
    yield

assert isinstance(
