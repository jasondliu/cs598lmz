import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class A:
    def f(self):
        pass
assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class B:
    def f(self):
        pass
b = B()
assert isinstance(b.f, types.MethodType)
assert isinstance(b.f, types.BuiltinMethodType)
assert not isinstance(b.f, types.FunctionType)
assert not isinstance(b.f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types
