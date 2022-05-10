gi = (i for i in ())
# Test gi.gi_code.co_flags as set in PyGen_New()
assert gi.gi_code.co_flags & (CO_FIB
