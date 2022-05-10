import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x, y: x, types.FunctionType)
assert isinstance(lambda x, y=1: x, types.FunctionType)
assert isinstance(lambda x, *y: x, types.FunctionType)
assert isinstance(lambda x, **y: x, types.FunctionType)
assert isinstance(lambda x, *y, **z: x, types.FunctionType)
assert isinstance(lambda x, y=1, *a, **b: x, types.FunctionType)
assert isinstance(lambda x, y=1, *a, **b: x, types.FunctionType)
assert isinstance(lambda x, y=1, *a, **b: x, types.FunctionType)
assert isinstance(lambda x, y=1, *a, **b: x, types.FunctionType)
assert isinstance(lambda x, y=1, *a, **
