import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(C().f, types.BuiltinMethodType)
assert not isinstance(C().f, types.FunctionType)
assert not is
