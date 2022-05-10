import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType
assert type(lambda x, y: x) is types.FunctionType
assert type(lambda x, y, z: x) is types.FunctionType
assert type(lambda x, y, z, t: x) is types.FunctionType
assert type(lambda x, y, z, t, u: x) is types.FunctionType
assert type(lambda x, y, z, t, u, v: x) is types.FunctionType
assert type(lambda x, y, z, t, u, v, w: x) is types.FunctionType
assert type(lambda x, y, z, t, u, v, w, a: x) is types.FunctionType
assert type(lambda x, y, z, t, u, v, w, a, b: x) is types.FunctionType
assert type(lambda x, y, z, t, u, v, w, a, b, c: x
