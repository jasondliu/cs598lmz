gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR flag
assert gi.gi_code.co_flags & 0x0020 == 0x0020
# Test gi.gi_frame.f_lasti == -1
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_stacktop == None
assert gi.gi_frame.f_stacktop == None
# Test gi.gi_frame.f_exc_traceback == None
assert gi.gi_frame.f_exc_traceback == None
# Test gi.gi_frame.f_exc_type == None
assert gi.gi_frame.f_exc_type == None
# Test gi.gi_frame.f_exc_value == None
assert gi.gi_frame.f_exc_value == None
# Test gi.gi_frame.f_restricted == False
assert gi.gi_frame.f_restricted == False

# Test gi.__next__() raises StopIteration
try:
    gi.__next__()

