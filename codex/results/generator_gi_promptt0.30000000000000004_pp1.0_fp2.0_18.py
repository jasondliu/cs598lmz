gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code is None)
# Test gi.gi_frame is None
print(gi.gi_frame is None)
# Test gi.gi_running is False
print(gi.gi_running is False)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom is None)

# Test gi.gi_frame.f_back is None
print(gi.gi_frame.f_back is None)
# Test gi.gi_frame.f_code is None
print(gi.gi_frame.f_code is None)
# Test gi.gi_frame.f_exc_traceback is None
print(gi.gi_frame.f_exc_traceback is None)
# Test gi.gi_frame.f_exc_type is None
print(gi.gi_frame.f_exc_type is None)
# Test gi.gi_frame.f_exc_value is None
print(gi.gi_frame.f_exc_value is None)
# Test gi.gi
