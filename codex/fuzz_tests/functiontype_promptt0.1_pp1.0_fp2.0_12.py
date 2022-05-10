import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance(3.14, types.FunctionType)
assert not isinstance('abc', types.FunctionType)
assert not isinstance(b'abc', types.FunctionType)
assert not isinstance(bytearray(b'abc'), types.FunctionType)
assert not isinstance(memoryview(b'abc'), types.FunctionType)
assert not isinstance(range(10), types.FunctionType)
assert not isinstance(iter(range(10)), types.FunctionType)
assert not isinstance(reversed(range(10)), types.FunctionType)
assert not isinstance(enumerate(range(10)), types.FunctionType)
assert not isinstance(zip(), types.FunctionType)
assert not isinstance(dict(), types.FunctionType)
assert not isinstance(set(), types
