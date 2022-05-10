gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.gi_frame.f_lasti is None
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno is None
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_locals is None
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_trace is None
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_code.co_argcount is None
print(gi.gi_frame.f_code.co_argcount)
# Test gi.gi_frame.f_code.co_cellvars is None

