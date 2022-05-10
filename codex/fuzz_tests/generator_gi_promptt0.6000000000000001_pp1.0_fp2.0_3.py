gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
try:
    gi.gi_await
except AttributeError:
    print("AttributeError")
# Test gi.gi_frame.f_code
gi.gi_frame.f_code
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno
# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals
# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace
# Test gi.gi_frame.f_back
gi.gi_frame.f_back
# Test gi.gi_frame.f_builtins
gi.gi_frame.f_builtins
# Test gi.
