gi = (i for i in ())
# Test gi.gi_code (a code object)
assert isinstance(gi.gi_code, types.CodeType)
assert gi.gi_code.co_filename == '<frozen generator>'

# Test gi.gi_frame (a frame or None)
assert isinstance(gi.gi_frame, types.FrameType)
assert gi.gi_frame.f_code is gi.gi_code
assert gi.gi_frame.f_lasti == 0
assert gi.gi_frame.f_lineno == 1
assert gi.gi_frame.f_back is None

# Test gi.gi_running (True or False)
assert not gi.gi_running

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.gi_frame.f_trace (function, generator or None)
assert gi.gi_frame.f_trace is None

# Test gi.throw()
try:
    gi.throw(ZeroDivisionError)
except ZeroDivisionError:
    pass
else
