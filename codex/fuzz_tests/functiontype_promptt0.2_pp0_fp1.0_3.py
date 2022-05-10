import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.FunctionType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(abs, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)
assert not isinstance(a.f, types.FunctionType)
assert not isinstance(a.f, types.BuiltinFunctionType)
assert not isinstance(a.f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(A.__init__, types.BuiltinMethodType)
assert not isinstance(A.
