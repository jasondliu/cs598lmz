fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
assert hash(gi.gi_code) == hash(fn.__code__)
