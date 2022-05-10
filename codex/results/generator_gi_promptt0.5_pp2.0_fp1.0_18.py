gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test gi.gi_code.co_freevars
print(gi.gi_code.co_freevars)

# Test gi.gi_code.co_cellvars
print(gi.gi_code.co_cellvars)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & 0x20)

# Test gi.gi_frame.f_code.co_freevars
print(gi.gi_frame.f_code.co_freevars)

# Test gi.gi_frame.f_code.co_cellvars
print(gi.gi_frame.f_code.co_cellvars)

# Test gi.gi_frame.f_code.co_nlocals
print(gi.gi_frame.f_code.co_nlocals)

# Test gi.gi_frame.f_code.co
