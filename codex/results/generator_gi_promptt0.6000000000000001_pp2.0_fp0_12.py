gi = (i for i in ())
# Test gi.gi_code is None.
assert gi.gi_code is None
# Test gi.gi_frame is None.
assert gi.gi_frame is None
# Test gi.gi_running is False.
assert not gi.gi_running
# Test gi.gi_yieldfrom is None.
assert gi.gi_yieldfrom is None
# Test gi.gi_weakreflist is empty.
assert len(gi.gi_weakreflist) == 0

# Test gi.gi_frame.f_code is None.
assert gi.gi_frame.f_code is None
# Test gi.gi_frame.f_builtins is empty.
assert len(gi.gi_frame.f_builtins) == 0
# Test gi.gi_frame.f_globals is empty.
assert len(gi.gi_frame.f_globals) == 0
# Test gi.gi_frame.f_lasti is -1.
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_
