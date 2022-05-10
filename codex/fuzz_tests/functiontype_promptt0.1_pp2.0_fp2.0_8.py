import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)
assert not isinstance(A.f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(A.__init__, types.BuiltinMethodType)
assert not isinstance(A.__init__, types
