import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(b"", types.FunctionType)
assert not isinstance(u"", types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(1.0, types.BuiltinFunctionType)
assert not isinstance("", types.BuiltinFunctionType)
assert not isinstance(b"", types.BuiltinFunctionType)
assert not isinstance(u"", types.BuiltinFunctionType)
assert not isinstance(f, types
