fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 'b'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (c1, c2)
fn.__annotations__ = {'a': 'b'}
fn.__kwdefaults__ = {'a': 'b'}
fn.__globals__ = {'a': 'b'}
fn.__module__ = 'mod'
fn.__qualname__ = 'qualname'

# Test __code__
assert fn.__code__ is gi.gi_code

# Test __name__
assert fn.__name__ == 'fn'

# Test __doc__
assert fn.__doc__ == 'doc'

# Test __dict__
assert fn.__dict__ == {'a': 'b'}

# Test __defaults__
assert fn.__defaults__ == (1, 2, 3)

# Test __closure__
assert
