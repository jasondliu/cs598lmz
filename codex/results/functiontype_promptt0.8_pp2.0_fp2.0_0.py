import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType) is True
assert isinstance(lambda x:x, types.FunctionType) is True

def g(): pass
def h(): pass
assert isinstance(f, type(g)) is True
assert isinstance(g, type(g)) is True
assert isinstance(h, type(g)) is True
assert isinstance(lambda x:x, type(lambda x:x)) is True

assert isinstance(f, type(h)) is True
assert isinstance(g, type(h)) is True
assert isinstance(h, type(h)) is True
assert isinstance(lambda x:x, type(lambda x:y:x+y)) is True

assert isinstance(f, type(lambda x:x)) is True
assert isinstance(g, type(lambda x:x)) is True
assert isinstance(h, type(lambda x:x)) is True
assert isinstance(lambda x:x, type(lambda x:x)) is True

assert isinstance(f, type(lambda x,y:x+y))
