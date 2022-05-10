import types
# Test types.FunctionType
assert isinstance(f1, types.FunctionType)
assert isinstance(f2, types.FunctionType)
assert isinstance(g1, types.FunctionType)
assert isinstance(g2, types.FunctionType)
assert isinstance(g3, types.FunctionType)
assert isinstance(g4, types.FunctionType)
assert isinstance(g5, types.FunctionType)
assert isinstance(g6, types.FunctionType)
assert isinstance(g7, types.FunctionType)
assert isinstance(g8, types.FunctionType)
assert not isinstance(g9, types.FunctionType)
assert not isinstance(g10, types.FunctionType)
assert not isinstance(g11, types.FunctionType)

# Test types.LambdaType
assert isinstance(f1, types.LambdaType)
assert not isinstance(f2, types.LambdaType)
assert isinstance(g1, types.LambdaType)
assert isinstance(g2, types.LambdaType)
assert isinstance(g3, types.Lamb
