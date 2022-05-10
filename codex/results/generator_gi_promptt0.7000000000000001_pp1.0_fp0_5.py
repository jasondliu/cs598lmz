gi = (i for i in ())
# Test gi.gi_code
print gi.gi_code
print gi.gi_code.co_code
print gi.gi_code.co_filename
# Test gi.gi_frame
print gi.gi_frame
print gi.gi_frame.f_code
print gi.gi_frame.f_code.co_code
print gi.gi_frame.f_code.co_filename
