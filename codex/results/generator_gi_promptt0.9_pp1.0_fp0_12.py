gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
# Test gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals
# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace
# Test sending a value to gi
gi.send(1)
