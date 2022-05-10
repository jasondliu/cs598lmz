import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x=1: x, types.FunctionType)
assert not isinstance(lambda *args: None, types.FunctionType)
assert not isinstance(lambda **kwargs: None, types.FunctionType)
assert not isinstance(lambda *args, **kwargs: None, types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x=1: x, types.LambdaType)
assert isinstance(lambda *args: None, types.LambdaType)
assert isinstance(lambda **kwargs: None, types.LambdaType)
assert isinstance(lambda *args, **kwargs: None, types.
