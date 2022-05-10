gi = (i for i in ())
# Test gi.gi_code: code object or NULL.
assert gi.gi_code is None

# Test gi.gi_frame: frame object or NULL.
with raises(TypeError):
    gi.gi_frame

# Test gi.gi_running: true if generator is running.
assert not gi.gi_running

# Test gi.gi_yieldfrom: the yielded-from generator.
assert gi.gi_yieldfrom is None

# Test gi.gi_weakreflist: list of weak references.
with raises(AttributeError):
    gi.gi_weakreflist

# Test gi.gi_exc_state.exc_type.
assert gi.gi_exc_state.exc_type is None

# Test gi.gi_exc_state.exc_value.
assert gi.gi_exc_state.exc_value is None

# Test gi.gi_exc_state.exc_traceback.
assert gi.gi_exc_state.exc_traceback is None

# Test gi.gi_exc_state.
