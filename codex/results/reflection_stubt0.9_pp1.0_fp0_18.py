fn = lambda: None
gi = (i for i in ())
fn.__code__ = cls.__call__.__code__
gi.gi_code = fn.__code__
# Call frame, frame function, and frame globals are all empty.
cf = gi.gi_frame
fn.__globals__ = {'foo': 'bar'}
fn.__code__ = type(fn.__code__)
cf.f_code = fn.__code__
assert cf.f_globals is fn.__globals__
# It works now!
assert cls.__new__(cls).from_callframe(cf) == ('bar',)


# f_locals needs to be set as well
fn.__code__ = ast.parse("return test + 3", mode='eval').body.args
fn.__globals__ = {'test': 17}
cf.f_code = fn.__code__
cf.f_locals = {}
cf.f_globals = fn.__globals__
assert cls.__new__(cls).from_callframe(cf) == (20,)


# Test the default
