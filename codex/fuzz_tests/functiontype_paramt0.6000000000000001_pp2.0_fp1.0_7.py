from types import FunctionType
list(FunctionType(lambda: 0, {}, '', (), None))

# Test __code__
# Verify that the function code object is correctly set up.
def f(x):
    return x+1
assert type(f.__code__) is code
assert f.__code__.co_argcount == 1
assert f.__code__.co_varnames == ('x',)
assert f.__code__.co_freevars == ()
assert f.__code__.co_cellvars == ()

def f(a, b, c, d):
    return a+b+c+d
assert type(f.__code__) is code
assert f.__code__.co_argcount == 4
assert f.__code__.co_varnames == ('a', 'b', 'c', 'd')
assert f.__code__.co_freevars == ()
assert f.__code__.co_cellvars == ()

def f(a, b, c, d, e):
    return a+b+c+d+e
assert type(f.
