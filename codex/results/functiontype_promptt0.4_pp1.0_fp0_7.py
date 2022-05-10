import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(int, type)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinMethodType)
assert isinstance(int, types.MethodType)
assert isinstance(int, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(int.__abs__, types.MethodType)
assert isinstance(int.__abs__, types.BuiltinMethodType)
assert isinstance(int.__add__, types.MethodType)
assert isinstance(int.__add__, types.BuiltinMethodType)
assert isinstance(int.__and__, types.MethodType)
assert isinstance(int.__and__, types.BuiltinMethodType)
assert isinstance(int.__call__, types.MethodType)
assert isinstance(int.__call__, types.BuiltinMethodType)
assert isinstance(int.__cmp__, types.MethodType)
assert isinstance(int.
