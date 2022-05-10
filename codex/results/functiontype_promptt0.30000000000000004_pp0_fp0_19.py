import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert type(f) is types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) == types.MethodType
assert isinstance(C.f, types.
