gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & CO_GENERATOR

# Test gi.gi_frame
assert gi.gi_frame.f_lasti == -1
assert gi.gi_frame.f_code.co_name == '<genexpr>'

# Test gi.gi_running
assert not gi.gi_running

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {'i': None}

# Test gi.gi_frame.f_back
assert gi.gi_frame.f_back is None

# Test gi.gi_frame.f_trace
assert gi.gi_frame.f_trace is None

# Test gi.gi_frame.f_exc_traceback
assert gi.gi_frame.f_exc_traceback is None

# Test gi.gi_frame.f_exc_type
