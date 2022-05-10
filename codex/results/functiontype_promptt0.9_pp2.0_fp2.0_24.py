import types
# Test types.FunctionType and types.LambdaType
def f():
    pass
def g():
    return lambda: 1

# set('abc', 'bcd') returns set([])
def assert_raises(exc_type, func, *args, **kw):
    try:
        func(*args, **kw)
    except exc_type:
        pass
    else:
        raise AssertionError("not raised")

x = set('abc')
assert type(x) is set, repr(type(x))
try:
    set()
except TypeError:
    pass
else:
    raise AssertionError
assert_raises(TypeError, set, [1,2,3], [2])
assert x == set(['a', 'c', 'b'])
assert len(x) == 3
assert 'a' in x
assert 'x' not in x
y = set(['a', 'c', 'd', 'd', 'd'])
assert y == set(['d', 'a', 'c'])
assert x != y
assert x <= y
assert x <
