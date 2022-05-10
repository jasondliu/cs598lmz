gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None

# Test gi.gi_frame
assert gi.gi_frame is None

# Test gi.gi_running
assert gi.gi_running is False

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.gi_name
assert gi.gi_name == '<genexpr>'

# Test gi.gi_qualname
assert gi.gi_qualname == '<genexpr>'

# Test gi.gi_weakreflist
assert gi.gi_weakreflist == []

# Test gi.gi_exc_state
assert gi.gi_exc_state == (None, None, None)

# Test gi.gi_exc_traceback
assert gi.gi_exc_traceback is None

# Test gi.gi_exc_type
assert gi.gi_exc_type is None

# Test gi.gi_exc_value
assert gi.gi_exc_value is
