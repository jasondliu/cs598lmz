gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is not None
print(gi.gi_frame)
# Test gi.gi_frame.f_code is None
print(gi.gi_frame.f_code)
# Test gi.gi_frame.f_back is not None
print(gi.gi_frame.f_back)
# Test gi.gi_frame.f_back.f_code is None
print(gi.gi_frame.f_back.f_code)
# Test gi.gi_frame.f_back.f_back is None
print(gi.gi_frame.f_back.f_back)
