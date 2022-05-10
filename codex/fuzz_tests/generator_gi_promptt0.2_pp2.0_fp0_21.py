gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & CO_GENERATOR == CO_GENERATOR

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 1

# Test gi.gi_frame.f_trace
def trace(frame, event, arg):
    pass

gi.gi_frame.f_trace = trace
assert gi.gi_frame.f_trace == trace

# Test gi.gi_frame.f_code
assert gi.gi_frame.f_code == gi.gi_code

# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}

# Test gi.gi_frame.f_globals
assert gi.gi_frame.f_globals == globals()

# Test gi.gi_frame.f_back

