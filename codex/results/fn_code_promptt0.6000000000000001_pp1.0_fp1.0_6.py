fn = lambda: None
# Test fn.__code__.co_varnames
def f(x, y, z): pass
fn.__code__ = f.__code__
assert fn.__code__.co_varnames == ('x', 'y', 'z')
assert fn.__code__.co_argcount == 3

# Test fn.__code__.co_cellvars
assert (lambda x: lambda y: x).__code__.co_cellvars == ('x',)

# Test fn.__code__.co_freevars
def f():
    x = 1
    y = 2
    def g():
        return x + y
    return g
fn = f()
assert fn.__code__.co_freevars == ('x', 'y')

# Test fn.__code__.co_filename
assert f.__code__.co_filename == __file__

# Test fn.__code__.co_firstlineno
assert f.__code__.co_firstlineno == inspect.currentframe().f_lineno - 1

# Test fn.__code__.co_
