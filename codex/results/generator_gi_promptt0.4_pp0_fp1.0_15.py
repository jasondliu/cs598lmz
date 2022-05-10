gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & 0x20 == 0x20

# Test gi.gi_frame.f_code.co_flags
assert gi.gi_frame.f_code.co_flags & 0x20 == 0x20

# Test gi.gi_frame.f_back.f_code.co_flags
assert gi.gi_frame.f_back.f_code.co_flags & 0x20 == 0x20

# Test gi.gi_frame.f_back.f_back.f_code.co_flags
assert gi.gi_frame.f_back.f_back.f_code.co_flags & 0x20 == 0x20

# Test gi.gi_frame.f_back.f_back.f_back.f_code.co_flags
assert gi.gi_frame.f_back.f_back.f_back.f_code.co_flags & 0x20 == 0x20

# Test gi.gi_frame.f_back.
