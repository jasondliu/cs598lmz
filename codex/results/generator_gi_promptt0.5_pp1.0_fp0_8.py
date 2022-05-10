gi = (i for i in ())
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ('i',)
# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}
# Test gi.gi_frame.f_globals
assert gi.gi_frame.f_globals == globals()

# Test gi.gi_frame.f_back
gi.gi_frame.f_back = None
assert gi.gi_frame.f_back == None

# Test gi.gi_frame.f_code
gi.gi_frame.f_code = None
assert gi.gi_frame.f_code == None

# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace = None
assert gi.gi_frame.f_trace == None

# Test gi.gi_running
gi.gi_running = 1
assert gi.gi_running == 1

# Test gi.gi_yieldfrom
gi.gi_yieldfrom
