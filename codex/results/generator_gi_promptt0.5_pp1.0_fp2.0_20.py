gi = (i for i in ())
# Test gi.gi_code is a function object
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code is gi.gi_code
# Test gi.gi_frame is a frame object
assert gi.gi_frame.f_back is None
assert gi.gi_frame.f_code.co_name == '<genexpr>'
assert gi.gi_frame.f_locals is gi.gi_frame.f_globals is __builtins__
# Test gi.gi_frame.f_lasti is an integer
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None

# Test gi.__name__ is a string
assert gi.__name__ == '<genexpr>'

# Test gi.__qualname__ is a string
assert gi.__qualname__ == '<genexpr>'

# Test gi.close raises a RuntimeError
try:
