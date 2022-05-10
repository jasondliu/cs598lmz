gi = (i for i in ())
# Test gi.gi_code is None
assert gi.gi_code is None
print(gi.gi_frame)
assert gi.gi_frame is None
