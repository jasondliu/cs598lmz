fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__globals__ = {'b': 2}
fn.__closure__ = (c1, c2)
fn.__annotations__ = {'c': 3}
fn.__kwdefaults__ = {'d': 4}
fn.__module__ = 'mod'
fn.__qualname__ = 'qualname'

print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__globals__)
print(fn.__closure__)
print(fn.__annotations__)
print(fn.__kwdefaults__)
print(fn.__module__)
print(fn.__qualname__)

# <code object <genexpr> at 0x00000
