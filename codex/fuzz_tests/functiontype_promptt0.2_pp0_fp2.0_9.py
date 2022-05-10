import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType
assert type(f) is not types.BuiltinFunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) is not types.BuiltinMethodType
assert type(f) != types.BuiltinMethodType
assert type(f) is not types.MethodType
assert type(f) != types.MethodType
assert type(f) is not types.ModuleType
assert type(f) != types.ModuleType
assert type(f) is not types.TypeType
assert type(f) != types.TypeType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) is not types.FunctionType
assert type(len) != types.FunctionType
assert type(len) is not types.BuiltinMethodType
assert type(len) != types.BuiltinMethodType
assert type(len) is not types.MethodType
assert type(len) !=
