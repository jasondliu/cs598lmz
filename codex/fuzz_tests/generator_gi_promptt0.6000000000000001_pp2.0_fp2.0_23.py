gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code is None)
# Test gi.gi_frame
print(gi.gi_frame is None)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom is None)
