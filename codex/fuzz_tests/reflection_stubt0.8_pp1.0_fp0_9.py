fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 1, 2, gi, gi, gi, 0, b'', (), (), '', '')
fn.__name__ = 'file'
fn.__doc__ = 'docstring'
fn.__dict__ = dict(a=1)
fn.__defaults__ = (1, 1)
fn.__globals__ = {}
fn.__closure__ = (lambda: 1, lambda: 1)
fn.__annotations__ = {'a': 1}

print(fn.__code__)
print(fn.__code__.co_nlocals)
print(fn.__code__.co_argcount)
print(fn.__code__.co_kwonlyargcount)
print(fn.__code__.co_stacksize)
print(fn.__code__.co_flags)
print(fn.__code__.co_code)
print(fn.__code__.co_consts)
print(fn.__code__.co_names)
print(fn.__code__.co_varnames)
print(
