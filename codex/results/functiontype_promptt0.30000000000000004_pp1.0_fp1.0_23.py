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
g = lambda: None
assert isinstance(g, types.LambdaType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)

# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)
assert not isinstance(h, types.FunctionType)
assert not isinstance(h, types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.
