fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Test that the code object is not modified
