gi = (i for i in ())
# Test gi.gi_code = getattr(gi, 'gi_code', None)
gi.gi_code = gi.gi_code
# Test gi.gi_code = getattr(gi, 'gi_code', None)
gi.gi_code = None
# Test gi.gi_frame = getattr(gi, 'gi_frame', None)
gi.gi_frame = gi.gi_frame
# Test gi.gi_frame = getattr(gi, 'gi_frame', None)
gi.gi_frame = None
# Test gi.gi_running = getattr(gi, 'gi_running', None)
gi.gi_running = gi.gi_running
# Test gi.gi_running = getattr(gi, 'gi_running', None)
gi.gi_running = None
try:
    # Test gi.gi_running = getattr(gi, 'gi_running', None)
    gi.gi_running = False
except AttributeError:
    pass
else:
    assert False, "assigning to .gi_running should raise AttributeError"


