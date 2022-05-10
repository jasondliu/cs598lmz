import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x, y: x, types.FunctionType)
assert not isinstance(lambda x, y, z: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w, v: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w, v, u: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w, v, u, t: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w, v, u, t, s: x, types.FunctionType)
assert not isinstance(lambda x, y, z, w, v, u, t, s, r: x, types.FunctionType)
assert not isinstance
