import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(type, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(b"", types.FunctionType)
assert not isinstance(u"", types.FunctionType)
assert not isinstance([], types.FunctionType)
assert not isinstance((), types.FunctionType)
assert not isinstance({}, types.FunctionType)
assert not isinstance(set(), types.FunctionType)
assert not isinstance(frozenset(), types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)

class C:
    def f():
        pass

assert not isinstance(C.f, types.FunctionType)
assert isinstance(C().
