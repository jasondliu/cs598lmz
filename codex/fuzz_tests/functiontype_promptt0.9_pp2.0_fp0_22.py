import types
# Test types.FunctionType is the same as function
assert isinstance(types.FunctionType, type)
assert isinstance(types.FunctionType, type(lambda: None))

# Test types.FunctionT
