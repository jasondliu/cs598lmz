import types
# Test types.FunctionType
def foo():
    return 0

assert isinstance(foo, types.FunctionType)
assert isinstance(foo, types.BuiltinFunctionType)
assert isinstance(foo, types.BuiltinMethodType)
assert isinstance(foo, types.MethodType)
assert not isinstance(foo, types.LambdaType)

# Test types.LambdaType
x = lambda: 1
assert isinstance(x, types.LambdaType)
assert not isinstance(x, types.FunctionType)
assert not isinstance(x, types.BuiltinFunctionType)
assert not isinstance(x, types.BuiltinMethodType)
assert not isinstance(x, types.MethodType)

# Test types.MethodType
class C:
    def foo(self):
        return 0

c = C()
assert not isinstance(c.foo, types.FunctionType)
assert not isinstance(c.foo, types.LambdaType)
assert not isinstance(c.foo, types.BuiltinFunctionType)
assert not isinstance(c.foo, types.BuiltinMethod
