import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(lambda x: x, types.CodeType)
assert isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
# Test types.BuiltinFunctionType
assert not isinstance(list, types.FunctionType)
assert not isinstance(list, types.LambdaType)
assert not isinstance(list, types.CodeType)
assert isinstance(list, types.BuiltinFunctionType)
assert not isinstance(list, types.BuiltinMethodType)
# Test types.BuiltinMethodType
assert not isinstance([].append, types.FunctionType)
assert not isinstance([].append, types.LambdaType)
assert not isinstance([].append, types.CodeType)
assert isinstance([].append, types.BuiltinFunctionType)
assert isinstance([].append, types.BuiltinMethodType)
# Test types.MethodType
assert not
