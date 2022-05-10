fn = lambda: None
# Test fn.__code__ exists
fn.__code__

# Test fn.__code__.co_varnames exists
fn.__code__.co_varnames

# Test fn.__code__.co_varnames is a tuple
isinstance(fn.__code__.co_varnames, tuple)

# Test that __code__ is a named tuple
from collections import namedtuple
isinstance(fn.__code__, namedtuple)
