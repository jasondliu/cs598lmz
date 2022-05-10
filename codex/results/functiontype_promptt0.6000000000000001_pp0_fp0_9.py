import types
# Test types.FunctionType
def foo(): pass
assert type(foo) == types.FunctionType
assert isinstance(foo, types.FunctionType)
assert type(foo) != types.LambdaType
assert not isinstance(foo, types.LambdaType)
# Test types.LambdaType
bar = lambda: None
assert type(bar) == types.LambdaType
assert isinstance(bar, types.LambdaType)
assert type(bar) != types.FunctionType
assert not isinstance(bar, types.FunctionType)
