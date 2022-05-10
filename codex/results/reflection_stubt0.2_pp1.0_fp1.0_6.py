fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__annotations__ = {'a': 1}
fn.__kwdefaults__ = {'a': 1}
fn.__globals__ = {'a': 1}
fn.__module__ = 'mod'

# test __repr__
print(fn)

# test __call__
fn()

# test __get__
fn.__get__(1)
fn.__get__(1, 2)

# test __set__
fn.__set__(1, 2)

# test __delete__
fn.__delete__(1)

# test __getattribute__
fn.__getattribute__('a')

# test __setattr__
fn.__setattr__('a', 1)

# test __delattr__
fn.
