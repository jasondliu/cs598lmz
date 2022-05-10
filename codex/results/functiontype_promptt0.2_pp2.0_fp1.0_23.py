import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert type(f) is not types.BuiltinFunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) is not types.MethodType
assert type(f) != types.MethodType
assert type(f) is not types.BuiltinMethodType
assert type(f) != types.BuiltinMethodType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) is not types.FunctionType
assert type(len) != types.FunctionType
assert type(len) is not types.MethodType
assert type(len) != types.MethodType
assert type(len) is not types.BuiltinMethodType
assert type(len) != types.BuiltinMethodType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) is types.MethodType
assert type(C
