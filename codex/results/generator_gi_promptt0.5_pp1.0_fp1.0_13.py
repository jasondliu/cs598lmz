gi = (i for i in ())
# Test gi.gi_code is not None
gi.gi_code

# Test that the code object is the same for gi and gi_code
assert gi.gi_code is gi_code
assert gi.gi_code is gi_code_2

# Test that the code object is the same for gi_code and gi_code_2
assert gi_code is gi_code_2

# Test that gi.gi_frame is None
assert gi.gi_frame is None

# Test that gi.gi_running is False
assert not gi.gi_running

# Test that gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None

# Test that gi.gi_frame.f_lasti is -1
assert gi.gi_frame.f_lasti == -1

# Test that gi.gi_frame.f_lineno is 0
assert gi.gi_frame.f_lineno == 0

# Test that gi.gi_frame.f_locals is {}
assert gi.
