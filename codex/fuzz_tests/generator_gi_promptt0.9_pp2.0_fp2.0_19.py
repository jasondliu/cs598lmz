gi = (i for i in ())
# Test gi.gi_code is None
assert gi.__code__ is None
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is 0
assert gi.gi_running is False
