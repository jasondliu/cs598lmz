gi = (i for i in ())
# Test gi.gi_code
TestError(gi.gi_code is None)

# Test gi.gi_frame
TestError(gi.gi_frame is None)

# Test gi.gi_running
TestError(gi.gi_running is None)

# Test gi.gi_yieldfrom
TestError(gi.gi_yieldfrom is None)

# Test gi.gi_weakreflist
TestError(gi.gi_weakreflist is None)
