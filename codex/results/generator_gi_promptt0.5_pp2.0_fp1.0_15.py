gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & 0x4

# Test gi.gi_running
gi.gi_running = True
assert gi.gi_running

# Test gi.gi_frame
assert gi.gi_frame == None

# Test gi.gi_frame.f_lineno
gi.gi_frame = frame
assert gi.gi_frame.f_lineno == 2

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == 0

# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace = trace
assert gi.gi_frame.f_trace == trace

# Test gi.gi_frame.f_exc_type
gi.gi_frame.f_exc_type = exc_type
assert gi.gi_frame.f_exc_type == exc_type

# Test gi.gi_frame.f_exc_value
gi.gi_frame.f_exc_value = exc_
