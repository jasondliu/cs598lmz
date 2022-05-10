fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del fn, gi

# print_function - needed for py2/3 compatibility
