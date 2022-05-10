gi = (i for i in ())
# Test gi.gi_code is None
print(next(gi, None) is None)

# Test gi.gi_frame is None
print(gi.gi_frame is None)

# Test gi.gi_running is 0
print(gi.gi_running == 0)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom is None)

# Test gi.gi_weakreflist is []
print(gi.gi_weakreflist == [])
