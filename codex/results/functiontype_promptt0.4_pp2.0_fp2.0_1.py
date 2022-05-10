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
    def m(self):
        pass

assert isinstance(A.m, types.MethodType)
assert isinstance(A.m, types.BuiltinMethodType)
assert not isinstance(A.m, types.BuiltinFunctionType)
assert not isinstance(A.m, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(map, types.BuiltinFunctionType)
assert isinstance(map, types.FunctionType)
assert not isinstance(map, types.BuiltinMethodType)
assert not isinstance(map, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(A().m, types.BuiltinMethodType)
assert isinstance(A().m, types.MethodType)
assert not is
