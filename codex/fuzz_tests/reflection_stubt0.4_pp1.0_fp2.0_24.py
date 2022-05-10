fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__module__ = 'bar'
fn.__doc__ = 'baz'
fn.__dict__ = {'qux': 'quux'}
fn.__defaults__ = (1, 2, 3)
fn.__kwdefaults__ = {'corge': 'grault'}
fn.__closure__ = (None,)
fn.__annotations__ = {'waldo': 'fred'}
fn.__globals__ = {'garply': 'waldo'}
fn.__qualname__ = 'plugh'

# Test that the repr() of a function with a __qualname__
# doesn't raise an exception
repr(fn)

# Test that the dir() of a function with a __qualname__
# doesn't raise an exception
dir(fn)

# Test that the str() of a function with a __qualname__
# doesn't raise an exception
str(fn)

# Test that the format() of a function with a __qualname__
# doesn't
