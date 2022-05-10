import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)
assert not isinstance(l, types.BuiltinFunctionType)
assert not isinstance(l, types.BuiltinMethodType)
assert not isinstance(l, types.MethodType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance
