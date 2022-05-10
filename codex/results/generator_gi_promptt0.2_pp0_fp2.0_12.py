gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & 0x20)

# Test gi.gi_frame.f_code.co_code
print(gi.gi_frame.f_code.co_code)

# Test gi.gi_frame.f_code.co_lnotab
print(gi.gi_frame.f_code.co_lnotab)

# Test gi.gi_frame.f_code.co_names
print(gi.gi_frame.f_code.co_names)

# Test gi.gi_frame.f_code.co_varnames
print(gi.gi_frame.f_code.co_varnames)

# Test gi.gi_frame.f_code.co_con
