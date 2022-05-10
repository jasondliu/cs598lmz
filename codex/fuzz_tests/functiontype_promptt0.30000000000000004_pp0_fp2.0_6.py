import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert issubclass(types.FunctionType, types.FunctionType)
assert not issubclass(object, types.FunctionType)
assert not issubclass(types.FunctionType, object)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert issubclass(types.BuiltinFunctionType, types.FunctionType)
assert not issubclass(object, types.BuiltinFunctionType)
assert not issubclass(types.BuiltinFunctionType, object)

# Test types.MethodType
class A(object):
    def f(self): pass
assert type(A.f) is types.MethodType
assert type(A.f) ==
