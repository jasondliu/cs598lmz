gi = (i for i in ())
# Test gi.gi_code, gi.gi_name and gi.gi_frame
assert gi.gi_code is None
assert gi.gi_name == '<genexpr>'
assert gi.gi_frame is None
