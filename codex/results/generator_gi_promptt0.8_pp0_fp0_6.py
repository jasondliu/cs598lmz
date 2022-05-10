gi = (i for i in ())
# Test gi.gi_code is NULL
gi.gi_code = None
gi.gi_frame
gi.gi_frame.f_code.co_name
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_lasti is NULL
gi.gi_frame.f_lasti = None
gi.gi_frame.f_code.co_name
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_code is NULL
gi.gi_frame.f_code = None
gi.gi_frame.f_code.co_name
gi.gi_frame.f_lasti

# Test gi.gi_frame is NULL
gi.gi_frame = None
gi.gi_frame.f_code.co_name
gi.gi_frame.f_lasti

"""
