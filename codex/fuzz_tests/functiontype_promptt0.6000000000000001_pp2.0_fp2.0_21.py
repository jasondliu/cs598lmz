import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert issubclass(types.FunctionType, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert type(id) == types.BuiltinFunctionType
assert isinstance(id, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert issubclass(types.TypeType, types.BuiltinFunctionType)
# Test types.TypeType
assert type(int) == types.TypeType
assert isinstance(int, types.TypeType)
assert issubclass(types.TypeType, object)
assert issubclass(type, types.TypeType)
assert issubclass(int, types.TypeType)
# Test types.TracebackType
try:
    raise ValueError
except ValueError:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
    assert isinstance
