fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__module__ = 'bar'
fn.__doc__ = 'baz'
fn.__dict__ = {'spam': 'ham'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (fn,)
fn.__annotations__ = {'spam': 'ham'}

# Test __repr__
print(repr(fn))

# Test __call__
fn()

# Test __get__
class C:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self):
        return self.fn

c = C(fn)
c()()

# Test __code__
print(fn.__code__)

# Test __name__
print(fn.__name__)

# Test __module__
print(fn.__module__)

# Test __doc__
print(fn.__doc__)

# Test __dict__
print(fn.__dict
