fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = code
fn.__name__ = gi.gi_name = 'spam'
fn.__qualname__ = gi.gi_qualname = 'spam'
fn.__annotations__ = gi.gi_annotations = {'ann': 'spam'}
fn.__closure__ = gi.gi_closure = (lambda: None,)
fn.__globals__ = gi.gi_frame.f_globals = {'spam': 'spam'}
fn.__dict__ = gi.gi_frame.f_locals = {}

# Flatten the function into tuples of data
flatfn = unflatten(flatten(fn))
flatgi = unflatten(flatten(gi))

# The flattened data should be completely equivalent
assert flatfn.__code__.co_code == fn.__code__.co_code
assert flatfn.__code__.co_consts == fn.__code__.co_consts
assert flatfn.__code__.co_names == fn.__code__.co_
