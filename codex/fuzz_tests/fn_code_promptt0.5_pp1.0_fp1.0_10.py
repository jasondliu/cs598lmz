fn = lambda: None
# Test fn.__code__ is a code object
fn.__code__ = 'foo'
# Test fn.__code__.co_varnames is a tuple
fn.__code__.co_varnames = 'foo'
# Test fn.__code__.co_varnames[0] is a string
fn.__code__.co_varnames = ('foo',)
# Test fn.__code__.co_argcount is an integer
fn.__code__.co_argcount = 'foo'

# Test fn.__code__.co_argcount is >= 0
fn.__code__.co_argcount = -1

# Test fn.__code__.co_argcount is <= co_varnames
fn.__code__.co_argcount = 2

# Test fn.__code__.co_argcount is <= co_varnames
fn.__code__.co_argcount = 1
fn.__code__.co_varnames = ('foo', 'bar', 'baz')

# Test fn.__code__.co_argcount is <= co_
