gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_GENERATOR)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & CO_GENERATOR)
# Test gi.gi_frame.f_back.f_code.co_flags
print(gi.gi_frame.f_back.f_code.co_flags & CO_GENERATOR)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_frame.f_back.f_code.co_name
print(gi.gi_frame.f_back.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)
# Test gi.gi_frame.f_back.f_code.co_filename
print(gi.gi_frame.f_
