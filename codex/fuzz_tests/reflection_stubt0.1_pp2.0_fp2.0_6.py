fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that the code object is not modified by the call.
assert gi.gi_frame is None
assert gi.gi_running is False

# Test that
