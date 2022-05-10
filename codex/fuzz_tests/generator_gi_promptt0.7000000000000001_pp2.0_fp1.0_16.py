gi = (i for i in ())
# Test gi.gi_code.co_code and gi.gi_frame.f_code.co_code
gi.gi_code.co_code == gi.gi_frame.f_code.co_code

# Test gi.gi_code.co_name and gi.gi_frame.f_code.co_name
gi.gi_code.co_name == gi.gi_frame.f_code.co_name

# Test gi.gi_code.co_filename and gi.gi_frame.f_code.co_filename
gi.gi_code.co_filename == gi.gi_frame.f_code.co_filename
