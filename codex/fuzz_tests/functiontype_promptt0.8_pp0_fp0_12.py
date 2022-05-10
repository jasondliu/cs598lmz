import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert issubclass(types.FunctionType, types.FunctionType)

# Test types.BuiltinFunctionType
def f(): pass
assert type(f) is not types.BuiltinFunctionType
assert type(pow) is types.BuiltinFunctionType
assert issubclass(types.BuiltinFunctionType, types.FunctionType)

# Test types.BuiltinMethodType (not supported by CPython)
def f(): pass
assert type(f) is not types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert issubclass(types.BuiltinMethodType, types.BuiltinFunctionType)
assert issubclass(types.BuiltinMethodType, types.MethodType)

# Test types.MethodType
def f(): pass
assert type(f) is not types.MethodType
x = []
assert type(x.append) is types.BuiltinMethodType
assert issubclass(types.MethodType, types.BuiltinFunctionType)

# Test types.ModuleType
assert type
