fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
assert fn.__code__ is gi.gi_code
assert fn.__name__ == 'fn'
assert fn.__doc__ == 'doc'
assert fn.__closure__ == gi.gi_closure
assert fn.__dict__ is gi.gi_frame.f_locals
assert fn.__annotations__ == gi.gi_frame.f_locals

# __code__ is not writable
try:
    fn.__code__ = 'abc'
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# __name__ is not writable
try:
    fn.__name__ = 'abc'
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# __doc__ is not writable
try:
    fn.__doc__ = 'abc'
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")


