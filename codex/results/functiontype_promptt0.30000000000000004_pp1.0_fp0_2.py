import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x, y: x, types.FunctionType)
assert isinstance(lambda x, y, z: x, types.FunctionType)
assert isinstance(lambda x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z: x, types.FunctionType)

try:
    isinstance(lambda x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa: x, types.FunctionType)
    assert False
except ValueError:
    pass

# Test types.BuiltinFunction
