import types
# Test types.FunctionType.
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)

def g():
    yield 1
assert not isinstance(g, types.FunctionType)
assert isinstance(g, types.GeneratorType)
assert not isinstance(g, types.LambdaType)
assert not isinstance(g, types.MethodType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)

l = lambda : 1
assert not isinstance(l, types.FunctionType)
assert not isinstance(l, types.GeneratorType)
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.MethodType)
assert not isinstance(l, types.Built
