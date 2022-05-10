fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'docstring'
fn.__module__ = 'module'
fn.__dict__ = {'__module__': 'module'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (c1, c2)
fn.__kwdefaults__ = {'a': 1, 'b': 2}
fn.__annotations__ = {'a': 1, 'b': 2}

# Verify that the function has all the expected attributes.
assert fn.__name__ == 'fn'
assert fn.__doc__ == 'docstring'
assert fn.__module__ == 'module'
assert fn.__dict__ == {'__module__': 'module'}
assert fn.__defaults__ == (1, 2, 3)
assert fn.__closure__ == (c1, c2)
assert fn.__kwdefaults__ == {'a': 1, 'b': 2}
assert fn.__annotations__ == {'a': 1, '
