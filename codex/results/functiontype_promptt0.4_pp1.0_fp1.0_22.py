import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance(1j, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(Exception, types.FunctionType)
assert not isinstance(Exception(), types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(NotImplemented, types.FunctionType)
assert not isinstance(Ellipsis, types.FunctionType)
assert not isinstance(slice, types.FunctionType)
assert not isinstance(Ellipsis, types.FunctionType)
assert not isinstance(slice(1, 2, 3), types.FunctionType)
assert not isinstance(xrange(10), types.FunctionType)
assert not isinstance
