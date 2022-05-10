fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__module__ = 'bar'
fn.__doc__ = 'baz'
fn.__dict__ = {'a': 1, 'b': 2}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__kwdefaults__ = {'a': 1, 'b': 2, 'c': 3}
fn.__annotations__ = {'a': 1, 'b': 2, 'c': 3}

print(fn)
print(fn.__code__)
print(fn.__name__)
print(fn.__module__)
print(fn.__doc__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__closure__)
print(fn.__kwdefaults__)
print(fn.__annotations__)
