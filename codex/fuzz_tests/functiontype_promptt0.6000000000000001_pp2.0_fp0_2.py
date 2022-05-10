import types
# Test types.FunctionType
assert isinstance(f, types.FunctionType)
# Test types.ClassType
assert isinstance(Foo, types.ClassType)
# Test types.MethodType
assert isinstance(Foo().f, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.InstanceType
assert isinstance(Foo(), types.InstanceType)
