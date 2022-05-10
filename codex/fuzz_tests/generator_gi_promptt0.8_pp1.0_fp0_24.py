gi = (i for i in ())
# Test gi.gi_code is None
assert gi.gi_code == None
# Test gi.gi_frame is the current frame
assert gi.gi_frame is gi.gi_frame.f_back

# Test gi.gi_running
gi = (i for i in ())
assert gi.gi_running == 0
gi.gi_frame.f_lasti = 0
assert gi.gi_running == 0
gi.gi_frame.f_lasti = -1
assert gi.gi_running == 0
gi.gi_frame.f_lasti = 1
assert gi.gi_running == 1
gi.gi_frame.f_lasti = 2
assert gi.gi_running == 2

# Test gi.gi_yieldfrom
gi = (i for i in ())
assert gi.gi_yieldfrom is None
# FIXME: we can't test gi.gi_yieldfrom at the moment because we can't
# create a generator-iterator directly (need to use something like
# iter(foo) or list(foo)
# gi.gi_
