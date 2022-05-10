gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_exc_type
print(gi.gi_frame.f_exc_type)

# Test gi.gi_frame.f_exc_value
print(gi.gi_frame.f_exc_value)

# Test gi.gi_frame.f_exc_traceback
print(gi.gi_frame.f_exc_traceback)

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lin
