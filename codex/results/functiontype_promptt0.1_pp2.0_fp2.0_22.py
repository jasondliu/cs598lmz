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
assert not isinstance(lambda x=1, *args: None, types.FunctionType)
assert not isinstance(lambda x=1, **kwargs: None, types.FunctionType)
assert not isinstance(lambda x=1, *args, **kwargs: None, types.FunctionType)
assert not isinstance(lambda x, y=1: None, types.FunctionType)
assert not isinstance(lambda x, y=1, *args: None, types.FunctionType)
assert not isinstance(lambda x, y=1, **kwargs: None, types.
