import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)
assert not isinstance(foo, types.MethodType)

# Test types.MethodType
class Foo(object):
    def foo(self): pass
assert isinstance(Foo().foo, types.MethodType)
assert not isinstance(Foo().foo, types.FunctionType)

# Test types.BuiltinMethodType
assert isinstance(int.__add__, types.BuiltinMethodType)
assert not isinstance(int.__add__, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert not isinstance((lambda: None), types.FunctionType)

# Test types.GeneratorType
assert isinstance((x for x in range(1)), types.GeneratorType)
assert not isinstance((x for x in range(1)), types.FunctionType)


