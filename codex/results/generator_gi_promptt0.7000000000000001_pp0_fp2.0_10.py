gi = (i for i in ())
# Test gi.gi_code is None on a "finished" generator
assert gi.gi_code is None
# Test gi.gi_frame is None on a "finished" generator
assert gi.gi_frame is None

# Test gi_code is not None on a generator in the middle of its execution
gi = (i for i in range(3))
next(gi)
assert gi.gi_code is not None

# Test gi_frame is not None on a generator in the middle of its execution
gi = (i for i in range(3))
next(gi)
assert gi.gi_frame is not None

# Test gi_running is not None on a generator in the middle of its execution
gi = (i for i in range(3))
next(gi)
assert gi.gi_running is not None

# Test gi_running is None on a "finished" generator
gi = (i for i in ())
assert gi.gi_running is None
