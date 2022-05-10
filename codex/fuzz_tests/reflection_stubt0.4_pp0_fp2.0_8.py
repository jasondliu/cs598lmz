fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'module'
fn.__dict__ = {'k': 'v'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__annotations__ = {'a': 'b'}
fn.__kwdefaults__ = {'k': 'v'}
print(fn)
print(fn())
