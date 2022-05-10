gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & 0x20

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_trace
assert gi.gi_frame.f_trace is None

# Test gi.gi_running
assert gi.gi_running == 0

# Test gi.gi_frame.f_code.co_argcount
assert gi.gi_frame.f_code.co_argcount == 0

# Test gi.gi_frame.f_code.co_consts
assert gi.gi_frame.f_code.co_consts == ()

# Test gi.gi_frame.f_code.co_flags
# XXX: the following assertion fails on the python3.3-3.3.2-32bit buildbot
#assert gi.gi_frame.f_code.co_flags == 67

# Test gi.gi_frame.f_code.co_first
