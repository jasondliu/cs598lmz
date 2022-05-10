import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(types.FunctionType, type)
assert issubclass(types.FunctionType, object)
