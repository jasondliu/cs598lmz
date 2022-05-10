fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = mock.Mock(co_argcount=1)
assert fn.__code__.co_argcount == 1

# Test fn.__code__.co_varnames
fn.__code__ = mock.Mock(co_varnames=('a', 'b'))
assert fn.__code__.co_varnames == ('a', 'b')

# Test fn.__code__.co_flags
fn.__code__ = mock.Mock(co_flags=0)
assert fn.__code__.co_flags == 0

# Test fn.__code__.co_defaults
fn.__code__ = mock.Mock(co_defaults=('a', 'b'))
assert fn.__code__.co_defaults == ('a', 'b')

# Test fn.__code__.co_kwonlyargcount
fn.__code__ = mock.Mock(co_kwonlyargcount=1)
assert fn.__code__.co_kwonlyargcount == 1

#
