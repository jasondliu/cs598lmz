import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)
assert isinstance(foo, types.BuiltinFunctionType)
assert not isinstance(foo, types.BuiltinMethodType)
assert not isinstance(foo, types.MethodType)

# Test types.MethodType
class A(object):
    def foo(self): pass
    @classmethod
    def bar(cls): pass
    @staticmethod
    def baz(): pass

a = A()
assert isinstance(a.foo, types.MethodType)
assert isinstance(A.foo, types.MethodType)
assert isinstance(a.bar, types.MethodType)
assert isinstance(A.bar, types.MethodType)
assert isinstance(a.baz, types.MethodType)
assert isinstance(A.baz, types.MethodType)
assert not isinstance(a.foo, types.BuiltinMethodType)
assert not isinstance(A.foo, types.BuiltinMethodType)
assert isinstance(a.bar, types.BuiltinMethodType)
assert isinstance(A
