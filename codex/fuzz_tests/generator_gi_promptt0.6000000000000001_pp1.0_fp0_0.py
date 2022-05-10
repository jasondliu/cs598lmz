gi = (i for i in ())
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_running
# Test gi.gi_frame
# Test gi.gi_frame.f_lasti
# Test gi.gi_frame.f_code.co_filename
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_lineno
# Test gi.gi_frame.f_trace

# Test gi.gi_yieldfrom

def f():
    yield from range(10)

# Test gi.gi_yieldfrom.gi_code.co_name
# Test gi.gi_yieldfrom.gi_frame.f_code.co_name
# Test gi.gi_yieldfrom.gi_running
# Test gi.gi_yieldfrom.gi_frame
# Test gi.gi_yieldfrom.gi_frame.f_lasti
# Test gi.gi_yieldfrom.gi_frame.f_code.co_filename
