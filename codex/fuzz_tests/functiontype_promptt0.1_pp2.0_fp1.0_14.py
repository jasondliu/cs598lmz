import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(str.upper, types.BuiltinMethodType)
assert not isinstance(str.upper, types.FunctionType)
assert not isinstance(str.
