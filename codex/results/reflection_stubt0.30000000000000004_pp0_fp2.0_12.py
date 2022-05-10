fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'module'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (2, 3)
fn.__closure__ = (4, 5)
fn.__annotations__ = {'a': 6}
fn.__kwdefaults__ = {'a': 7}

print(fn)
print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__module__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__closure__)
print(fn.__annotations__)
print(fn.__kwdefaults__)

# code
# fn
# doc
# module
# {'a': 1}
# (2, 3)
# (4, 5)
# {'a': 6}
# {'a': 7}
