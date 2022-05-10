gi = (i for i in ())
# Test gi.gi_code is a function object
assert isinstance(gi.gi_code, types.CodeType)
# Test gi.gi_code.co_name is an empty string
assert gi.gi_code.co_name == ''
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is 0
assert gi.gi_running == 0
# Test gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None

gi = (i for i in (1, 2, 3))
# Test gi.gi_code is a function object
assert isinstance(gi.gi_code, types.CodeType)
# Test gi.gi_code.co_name is an empty string
assert gi.gi_code.co_name == ''
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is 0
assert gi.gi_running == 0
# Test gi.gi_yieldfrom is None
assert gi.gi
