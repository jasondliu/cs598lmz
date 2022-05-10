fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename

# also works for other attributes
fn.__code__.co_varnames

# but not everything is allowed
