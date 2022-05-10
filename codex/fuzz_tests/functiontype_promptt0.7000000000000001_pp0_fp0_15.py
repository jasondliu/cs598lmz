import types
# Test types.FunctionType
def test_types_functiontype():
    def f(a, b):
        return a + b
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.MethodType)
    assert isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.LambdaType)
    assert not isinstance(f, types.GeneratorType)
test_types_functiontype()

# Test types.MethodType
class C:
    def f(self, a, b):
        return a + b
    def g(self, a, b):
        return a + b
c = C()
assert not isinstance(c.f, types.FunctionType)
assert isinstance(c.f, types.MethodType)
assert not isinstance(c.f, types.BuiltinFunctionType)
assert not isinstance(c.f, types.BuiltinMethodType)
assert not isinstance(c.f, types.LambdaType)
assert not
