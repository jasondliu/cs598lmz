import types
# Test types.FunctionType (not type 'function')
assert isinstance(print, types.FunctionType)
assert isinstance(print, type)
assert not isinstance(print, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, type)
assert not isinstance(len, types.FunctionType)
# Test types.MethodType (not type 'method')
assert isinstance((1).__add__, types.MethodType)
assert isinstance((1).__add__, type)
assert not isinstance((1).__add__, types.BuiltinMethodType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert isinstance([].append, type)
assert not isinstance([].append, types.MethodType)

# Test isinstance() with type objects which are classes (not instances or other objects).

assert isinstance(list, type)
assert not isinstance(list, object)
assert not isinstance(list, list)
assert not isinstance(list, (
