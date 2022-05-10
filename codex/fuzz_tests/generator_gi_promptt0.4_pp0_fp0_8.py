gi = (i for i in ())
# Test gi.gi_code is a function object
assert isinstance(gi.gi_code, types.CodeType)
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is False
assert gi.gi_running is False
# Test gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None
# Test gi.gi_name is '<genexpr>'
assert gi.gi_name == '<genexpr>'
# Test gi.gi_qualname is '<genexpr>'
assert gi.gi_qualname == '<genexpr>'
# Test gi.gi_weakreflist is None
assert gi.gi_weakreflist is None

# Test gi.gi_frame is None
gi = (i for i in ())
assert gi.gi_frame is None

# Test gi.gi_frame is None
gi = (i for i in ())
assert gi.gi_frame is None

# Test gi.gi_frame is None
gi =
