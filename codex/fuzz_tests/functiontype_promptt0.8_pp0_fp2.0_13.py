import types
# Test types.FunctionType()
f = types.FunctionType(lambda: 1)
assert f() == 1

f = types.FunctionType(lambda x: x + 1, globals())
assert f(42) == 42 + 1

f = types.FunctionType(lambda x: x + 1, globals(), 'f', (1,))
assert f(42) == 42 + 1
assert f.__code__.co_argcount == 1
assert f.__code__.co_varnames == ('x',)

f = types.FunctionType(lambda x: x + 1, globals(), 'f', (1,), {'c': 2})
assert f(42) == 42 + 1
assert f.__code__.co_argcount == 1
assert f.__code__.co_varnames == ('x',)
assert f.__closure__ is None
assert f.c == 2

def g(x):
    return x + 1
f = types.FunctionType(g.__code__, globals(), 'f', None, g.__closure__)
assert f.c == 2

