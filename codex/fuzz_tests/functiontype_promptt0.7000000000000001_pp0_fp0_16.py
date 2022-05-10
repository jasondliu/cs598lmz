import types
# Test types.FunctionType
def f(): return 1
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(lambda: None) == types.FunctionType
assert type(list.append) == types.BuiltinFunctionType
