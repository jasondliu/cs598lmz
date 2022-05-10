import types
# Test types.FunctionType
def foo(): pass
f = foo
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class Foo(object):
    def foo(self): pass
f = Foo()
f.foo()
assert isinstance(f.foo, types.MethodType)
assert not isinstance(f.foo, types.BuiltinFunctionType)
assert not isinstance(f.foo, types.BuiltinMethodType)
assert not isinstance(f.foo, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(foo, types.BuiltinFunctionType)
assert not isinstance(foo, types.FunctionType)
assert not isinstance(foo, types.BuiltinMethodType)
assert not isinstance(foo, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(f.foo, types.BuiltinMethodType)
assert not isinstance
