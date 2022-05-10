import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert not issubclass(types.FunctionType, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert not issubclass(object, types.FunctionType)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not issubclass(types.BuiltinFunctionType, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert not issubclass(object, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) is types.MethodType
assert isinstance(C.m, types.MethodType)
assert not issubclass(types.MethodType, types.MethodType)
assert issubclass(types.MethodType, object)
assert not issubclass(object, types.MethodType)

#
