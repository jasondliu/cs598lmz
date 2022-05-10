gi = (i for i in ())
# Test gi.gi_code is not set as it is freed immediately.
assert gi.gi_code is None

# test gi_frame is not set
gi = (i for i in ())
gi.gi_frame = 'should not be set'
assert gi.gi_frame is None
