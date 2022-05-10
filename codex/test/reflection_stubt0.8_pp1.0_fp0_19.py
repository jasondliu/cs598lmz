fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
try:
    fn()
except TypeError as e:
    pass

# Can't assign code to arbitrary objects - let's try a list:
