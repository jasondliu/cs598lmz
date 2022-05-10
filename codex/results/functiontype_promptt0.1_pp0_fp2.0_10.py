import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(b"", types.FunctionType)
assert not isinstance(bytearray(b""), types.FunctionType)
assert not isinstance(u"", types.FunctionType)
assert not isinstance(frozenset(), types.FunctionType)
assert not isinstance(set(), types.FunctionType)
assert not isinstance(dict(), types.FunctionType)
assert not isinstance(list(), types.FunctionType)
assert not isinstance(tuple(), types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(Exception(), types.FunctionType)
assert not isinstance(Exception, types.FunctionType)
