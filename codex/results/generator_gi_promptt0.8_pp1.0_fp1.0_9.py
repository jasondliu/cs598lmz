gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code == test_code

# Test gi.gi_frame
try:
    gi.gi_frame
except ValueError:
    pass
else:
    assert False

# Test gi.gi_running
gi.gi_running

# Test gi.gi_frame
assert gi.gi_frame is None

# Test gi.gi_running
assert isinstance(gi.gi_running, int)

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.gi_traceback
assert gi.gi_traceback is None

# Test gi.gi_exc_state
gi.gi_exc_state

# Test gi.gi_weakreflist
assert gi.gi_weakreflist == []

# Test gi.gi_finalizer
# TODO
# Test gi.gi_qualname
assert gi.gi_qualname is None

# Test gi.gi_running (once more, to check it still works)
