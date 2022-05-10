fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert gi.gi_code == fn.__code__
assert gi.gi_frame == fn.__code__.co_frame

# Test that the code object is not modified
assert gi.gi_code == fn.__code__
assert gi.gi_frame == fn.__code__.co_frame
