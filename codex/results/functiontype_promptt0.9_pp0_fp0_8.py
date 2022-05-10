import types
# Test types.FunctionType
f = FunctionType(0, 0, 0, 0, 0)
print(f)
assert isinstance(f, types.FunctionType)
# Test types.MethodType
m = MethodType(f, 0)
print(m)
assert isinstance(m, types.MethodType)
