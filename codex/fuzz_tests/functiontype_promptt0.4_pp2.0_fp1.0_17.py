import types
# Test types.FunctionType
def f(): pass
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
class C:
    def m(self): pass

assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.FunctionType)
assert not isinstance(C.m, types.BuiltinFunctionType)
assert not isinstance(C.m, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert not isinstance(list.append, types.FunctionType)
assert not isinstance
