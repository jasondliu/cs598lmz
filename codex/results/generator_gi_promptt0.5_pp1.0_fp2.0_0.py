gi = (i for i in ())
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<stdin>'
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 0
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 67
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<stdin>'
# Test gi.gi_frame.f_code.co_firstlineno
assert gi.gi_frame.f_code.co_firstlineno == 0
# Test gi.gi_frame.f_code.co_flags
assert gi.gi_frame.f_code.co_flags == 67

# Test gi.gi_running
gi = (i for i in ())
assert not gi.gi_running
gi.gi_frame.f_back = None
assert gi.gi_running
gi.gi_frame.f_back = g
