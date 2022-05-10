fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = 'code'
assert fn.__code__ == 'code'
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()
del fn.__code__
assert fn.__code__ == ()
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()
try:
    del fn.__code__
except AttributeError:
    pass
else:
    assert False, "Can delete fn.__code__"
# Test fn.__code__.co_varnames
fn.__code__ = 'code'
assert fn.__code__ == 'code'
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()
fn.__code__ = lambda: None
assert fn.__code__ == ()
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()

def f():
