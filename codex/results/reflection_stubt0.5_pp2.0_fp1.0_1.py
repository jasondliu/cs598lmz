fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test_name'
fn.__doc__ = 'test_doc'
fn.__dict__ = {}
fn.__defaults__ = (1, 2)
fn.__kwdefaults__ = {'a': 1, 'b': 2}
fn.__closure__ = (1,)
fn.__annotations__ = {'a': 1}
fn.__globals__ = {}
fn.__module__ = 'abc'
fn.__qualname__ = 'abc'
fn.__text_signature__ = 'abc'

print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__kwdefaults__)
print(fn.__closure__)
print(fn.__annotations__)
print(fn.__globals__)
print(fn.__module__)
print(fn.__qualname__)
print(fn.__text_sign
