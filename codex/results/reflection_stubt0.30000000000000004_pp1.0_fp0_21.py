fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__dict__ = {'baz': 'qux'}
fn.__defaults__ = (1, 2, 3)
fn.__globals__ = {'a': 1}
fn.__closure__ = (c,)
fn.__annotations__ = {'return': int}
fn.__kwdefaults__ = {'a': 1}
fn.__module__ = '__main__'
fn.__qualname__ = 'foo.bar'

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

# <code object <genexpr> at
