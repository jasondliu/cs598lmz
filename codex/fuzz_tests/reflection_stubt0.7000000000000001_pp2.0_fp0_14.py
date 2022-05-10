fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__module__ = 'baz'
fn.__defaults__ = fn.__closure__ = ()
fn.__dict__ = {}
print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__module__)
print(fn.__defaults__)
print(fn.__closure__)
print(fn.__dict__)

print(fn.__code__.co_code)
print(fn.__code__.co_consts)
print(fn.__code__.co_names)
print(fn.__code__.co_varnames)
print(fn.__code__.co_freevars)
print(fn.__code__.co_cellvars)
