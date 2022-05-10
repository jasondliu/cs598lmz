gi = (i for i in ())
# Test gi.gi_code is a code object
print(gi.gi_code.co_name)

# Test gi.gi_frame is a frame
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_back is None
print(gi.gi_frame.f_back)
