gi = (i for i in ())
# Test gi.gi_code.co_flags
print(next(gi).gi_code.__flags__)

# Test gi.gi_frame.f_code.co_flags
print(next(gi).gi_frame.f_code.__flags__)

# Test gi.gi_frame.f_back.f_code.co_flags
print(next(gi).gi_frame.f_back.f_code.__flags__)

# Test gi.gi_frame.f_back.f_back.f_code.co_flags
print(next(gi).gi_frame.f_back.f_back.f_code.__flags__)

# Test gi.gi_frame.f_back.f_back.f_back.f_code.co_flags
print(next(gi).gi_frame.f_back.f_back.f_back.f_code.__flags__)

# Test gi.gi_frame.f_back.f_back.f_back.f_back.f_code.co_flags
print(next(gi
