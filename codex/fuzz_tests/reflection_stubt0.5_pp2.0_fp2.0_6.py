fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn()

# Issue #12476: If a generator function is given a __qualname__,
# make sure it propagates to the generator object.
def gen_fn():
    yield

gen_fn.__qualname__ = 'foo.bar'
g = gen_fn()
assert g.__qualname__ == 'foo.bar'

# Issue #20808: A generator function should have a __module__
# attribute.
def gen_fn():
    yield

g = gen_fn()
assert g.__module__ == __name__

# Issue #20808: A generator function should have the same
# __module__ as the module its code was loaded from.
fn = lambda: None
fn.__code__ = g.gi_frame.f_code
assert fn.__module__ == __name__

# Issue #20808: A generator function should have the same
# __module__ as the module it was defined in.
fn = lambda:
