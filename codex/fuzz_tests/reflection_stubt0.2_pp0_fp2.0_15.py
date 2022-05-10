fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__globals__ = {'b': 2}
fn.__closure__ = (c,)
fn.__annotations__ = {'c': 3}
fn.__kwdefaults__ = {'d': 4}

# test_dir
print(dir(fn))

# test_repr
print(repr(fn))

# test_call
print(fn())

# test_getattr
print(fn.__name__)
print(fn.__doc__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__globals__)
print(fn.__closure__)
print(fn.__code__)
print(fn.__annotations__)
print(fn.__kwdefaults__)

# test_setattr
fn.__name__ =
