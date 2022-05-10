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
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)
assert not isinstance(A.f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
class B:
    def f(self):
        pass

assert isinstance(B.f, types.MethodType)
assert not isinstance(B.f, types.FunctionType)
assert not isinstance(B.f, types.BuiltinFunctionType)
assert isinstance(B.f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.Built
