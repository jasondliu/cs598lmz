gi = (i for i in ())
# Test gi.gi_code is not None
assert gi.gi_code is not None
# Test gi.gi_code.co_flags is not None
assert gi.gi_code.co_flags is not None
# Test gi.gi_code.co_flags & 0x20 is not None
assert gi.gi_code.co_flags & 0x20 is not None
# Test gi.gi_code.co_flags & 0x20 is 0
assert gi.gi_code.co_flags & 0x20 is 0
# Test gi.gi_code.co_flags & 0x20 is not 0
assert gi.gi_code.co_flags & 0x20 is not 0
# Test gi.gi_code.co_flags & 0x20 is not 0
assert gi.gi_code.co_flags & 0x20 is not 0
# Test gi.gi_code.co_flags & 0x20 is 0
assert gi.gi_code.co_flags & 0x20 is 0
# Test gi.gi_code.co_flags & 0x20 is not
