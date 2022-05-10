fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__closure__ = ()
fn.__globals__ = {}
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__module__ = 'baz'

# Test __setstate__
fn.__setstate__({})

# Test __getstate__
fn.__getstate__()

# Test __call__
fn()

# Test __repr__
fn.__repr__()

# Test __str__
fn.__str__()

# Test __get__
fn.__get__(1, 2)

# Test __getattribute__
fn.__getattribute__('__name__')

# Test __setattr__
fn.__setattr__('__name__', 'foo')

# Test __delattr__
fn.__delattr__('__name__')

# Test __hash__
hash(
