fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'mod'
fn.__dict__ = {'key': 'value'}
fn.__defaults__ = (1, 2, 3)
fn.__globals__ = {'key': 'value'}
fn.__closure__ = (gi,)
fn.__annotations__ = {'key': 'value'}
fn.__kwdefaults__ = {'key': 'value'}

# Function attributes
print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__module__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__globals__)
print(fn.__closure__)
print(fn.__annotations__)
print(fn.__kwdefaults__)

# Function call
print(fn())

# Function repr
print(repr(fn))

# Function str
