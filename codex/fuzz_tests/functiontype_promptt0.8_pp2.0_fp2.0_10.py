import types
# Test types.FunctionType for sanity's sake
g = lambda x: x
assert isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(list, types.BuiltinFunctionType)
# Test types.MethodType for sanity's sake
def f():
    pass
m = types.MethodType(f, None)
assert isinstance(m, types.MethodType)
assert not isinstance(f, types.MethodType)
# Test types.BuiltinMethodType
assert isinstance(list.__iter__, types.BuiltinMethodType)
assert not isinstance(list.__iter__, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(m, types.BuiltinMethodType)
assert not isinstance(g, types.BuiltinMethodType)
# Test types.UnboundMethodType
assert isinstance(list.__len__, types.UnboundMethodType)
assert not isinstance(list.__len__, types.BuiltinMethodType)
assert not isinstance(list.__len__,
