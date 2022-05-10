gi = (i for i in ())
# Test gi.gi_code == gi.__code__
print(gi.gi_code == gi.__code__)

# Test gi.gi_frame == gi.gi_running
print(gi.gi_frame == gi.gi_running)

# Test gi.gi_frame.f_lasti == gi.gi_frame.f_lineno
print(gi.gi_frame.f_lasti == gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_locals == gi.gi_frame.f_globals
print(gi.gi_frame.f_locals == gi.gi_frame.f_globals)

# Test gi.gi_frame.f_back == None
print(gi.gi_frame.f_back is None)

# Test gi.gi_frame.f_back == gi.gi_frame.f_back.f_back
print(gi.gi_frame.f_back == gi.gi_frame.f_back.f_back)

#
