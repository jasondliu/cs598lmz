gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x0040

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 1

# Test gi.gi_frame.f_trace
assert gi.gi_frame.f_trace is None

# Test gi.gi_frame.f_exc_traceback
assert gi.gi_frame.f_exc_traceback is None

# Test gi.gi_frame.f_exc_type
assert gi.gi_frame.f_exc_type is None

# Test gi.gi_frame.f_exc_value
assert gi.gi_frame.f_exc_value is None

# Test gi.gi_frame.f_builtins
assert gi.gi_frame.f_builtins is __builtins__

# Test gi.gi_frame.f_gl
