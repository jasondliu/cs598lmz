fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'attr': 'value'}

# Test that the function attributes are pickled correctly
data = pickle.dumps(fn)
fn2 = pickle.loads(data)
assert fn.__code__ is fn2.__code__
assert fn.__name__ == fn2.__name__
assert fn.__doc__ == fn2.__doc__
assert fn.__dict__ == fn2.__dict__

# Test that the function can be called
fn2()

# Test that the function can be pickled again
data2 = pickle.dumps(fn2)
assert data == data2

# Test that the function can be pickled with a different pickler
data = pickle.dumps(fn, pickle.HIGHEST_PROTOCOL)
fn2 = pickle.loads(data)
assert fn.__code__ is fn2.__code__
assert fn.__name__ == fn2.__name__

