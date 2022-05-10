gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)
print(gi.gi_code.co_flags & 0x40)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & 0x20)
print(gi.gi_frame.f_code.co_flags & 0x40)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)


