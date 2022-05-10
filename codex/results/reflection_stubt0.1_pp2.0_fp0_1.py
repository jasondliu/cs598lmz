fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__globals__ = {'a': 1}
fn.__annotations__ = {'a': 1}
fn.__kwdefaults__ = {'a': 1}
fn.__module__ = 'mod'

# Test __repr__
assert repr(fn) == '<function fn at 0x%x>' % id(fn)

# Test __call__
assert fn() is None

# Test __get__
assert fn.__get__(1) is fn
assert fn.__get__(1, 2) is fn

# Test __getattribute__
assert fn.__getattribute__('__name__') == 'fn'
assert fn.__getattribute__('__doc__') == 'doc'
assert fn.__getattribute__('__dict__') ==
