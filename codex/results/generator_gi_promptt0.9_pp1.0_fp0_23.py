gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_name
gi.gi_name
# Test gi.gi_frame
gi.gi_frame
gi.gi_frame is None
gi1 = (i for i in range(10))
# Test gi1.gi_frame
gi1.gi_frame
# Test gi1.gi_frame
gi1.gi_frame.f_back
# Test gi1.gi_frame.f_lasti
gi1.gi_frame.f_lasti
# Test gi1.gi_frame.f_locals
gi1.gi_frame.f_locals
# Test gi1.gi_frame.f_locals
len(gi1.gi_frame.f_locals)
# Test gi1.gi_frame.f_locals
gi1.gi_frame.f_locals['i']
# Test gi1.gi_frame.f_lineno

