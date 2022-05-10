gi = (i for i in ())
# Test gi.gi_code is not looked up if gi.gi_frame is None.
del gi.gi_frame  # leave builtin_frame
gi.gi_code = None
# Test getcode.
gi.gi_code = _testcode
code = gi.gi_code
assert code is _testcode
# Test getrunning
assert gi.gi_running is False
# Test gi_running.
gi.gi_code = _testcode
assert gi.gi_running is True
assert _testcode.gi_running is True
gi.gi_code = None
assert gi.gi_running is False
# Test getframe.
gi.gi_frame = One(sys._getframe())
frame = gi.gi_frame
assert frame is not None
assert frame.f_back is None
code = frame.f_code
assert code is _testcode
assert frame.f_globals is _testglobals
assert frame.f_locals is gi.gi_frame.f_locals
assert frame.f_trace is f.trace_dispatch

# Make sure frame
