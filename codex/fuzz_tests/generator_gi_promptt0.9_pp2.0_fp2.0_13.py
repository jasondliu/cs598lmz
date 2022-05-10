gi = (i for i in ())
# Test gi.gi_code is not NULL, because
# PyGen_NeedsFinalizing(gi) has a NULL check for gi->gi_code.
assert gi.gi_code is not None
assert PyGen_NeedsFinalizing(gi)
