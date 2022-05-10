fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__qualname__ = 'foo'
fn.__module__ = '__main__'
fn.__globals__ = globals()
fn.__closure__ = (c,)
fn.__annotations__ = {'a': 'b'}
fn.__kwdefaults__ = {'a': 'b'}
fn.__dict__ = {'a': 'b'}
fn.__text_signature__ = '(a, b)'

print(fn)
print(fn.__code__)
print(fn.__code__.co_code)
print(fn.__code__.co_names)
print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_cellvars)
print(fn.__code__.co_freevars)
print(fn.__code__.co_consts)
print(fn.__code__.co_filename)
print(fn
