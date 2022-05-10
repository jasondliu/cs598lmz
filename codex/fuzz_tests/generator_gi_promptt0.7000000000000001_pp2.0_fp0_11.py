gi = (i for i in ())
# Test gi.gi_code is None
assert next(gi) is None
assert not gi.gi_frame

# Test gi.gi_code is a code object
gi = (i for i in [1])
assert next(gi) == 1
assert gi.gi_frame.f_code is gi.gi_code
assert gi.gi_frame.f_lasti == 0

# Test gi.gi_code is a code object, with a send()
gi = (i for i in [1])
assert gi.send(None) == 1
assert gi.gi_frame.f_code is gi.gi_code
assert gi.gi_frame.f_lasti == 0

# Test gi.gi_code is None
gi = (i for i in [1])
assert next(gi) == 1
assert gi.gi_code is None

# Test gi.gi_c
