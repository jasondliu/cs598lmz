gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_GENERATOR)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & CO_GENERATOR)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_firstlineno
print(gi.gi_frame.f_code.co_firstlineno)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f
