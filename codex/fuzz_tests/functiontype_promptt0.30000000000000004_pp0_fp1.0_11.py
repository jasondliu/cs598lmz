import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance("".join, types.BuiltinMethodType)
assert not isinstance("".join, types.FunctionType)
assert not isinstance("".join, types.BuiltinFunctionType)
assert not isinstance("".join, types.MethodType)

# Test types.MethodType
class C(object):
    def m(self): pass
assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.FunctionType)
assert not isinstance(C.m, types
