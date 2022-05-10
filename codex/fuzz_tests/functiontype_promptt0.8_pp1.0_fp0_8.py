import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x=x: x, types.FunctionType)
assert not isinstance([], types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x=x: x, types.LambdaType)
assert not isinstance([], types.LambdaType)

# Test types.GeneratorType
def g():
    yield

assert not isinstance(f, types.GeneratorType)
assert not isinstance(lambda x: x, types.GeneratorType)
assert not isinstance([], types.GeneratorType)
assert isinstance(g(), types.GeneratorType)


def test_types_str():
    assert isinstance(str(types.MethodType.__call__), str)


class C:
    pass

c = C
