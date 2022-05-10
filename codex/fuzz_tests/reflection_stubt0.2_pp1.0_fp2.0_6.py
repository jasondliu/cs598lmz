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

# test __repr__
assert repr(fn) == '<function fn at 0x%x>' % id(fn)

# test __call__
assert fn() is None

# test __get__
assert fn.__get__(1) is fn
assert fn.__get__(1, 2) is fn

# test __getattribute__
assert fn.__getattribute__('__name__') == 'fn'
assert fn.__getattribute__('__module__') == 'mod'
assert fn.__getattribute__('__doc__') ==
