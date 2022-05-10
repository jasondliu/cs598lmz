import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(b"", types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance((), types.FunctionType)
assert not isinstance([], types.FunctionType)
assert not isinstance({}, types.FunctionType)
assert not isinstance(set(), types.FunctionType)
assert not isinstance(frozenset(), types.FunctionType)
assert not isinstance(object(), types.FunctionType)

# Test types.GeneratorType

def f():
    yield 1

assert isinstance(f(), types.GeneratorType)
assert not isinstance(None, types.GeneratorType)
assert not isinstance(1, types.GeneratorType)
assert not isinstance("", types.GeneratorType)
assert
