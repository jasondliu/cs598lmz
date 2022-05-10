gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_GENERATOR)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_globals
print(gi.gi_frame.f_globals)

# Test gi.gi_frame.f_back

