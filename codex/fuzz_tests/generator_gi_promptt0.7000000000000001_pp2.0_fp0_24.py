gi = (i for i in ())
# Test gi.gi_code (code object)
assert gi.gi_code.co_filename == __file__
assert gi.gi_code.co_name == '<genexpr>'

# Test gi.gi_frame (frame object)
assert gi.gi_frame.f_code.co_filename == __file__
assert gi.gi_frame.f_code.co_name == '<module>'
assert gi.gi_frame.f_lasti == 0

# Test gi.gi_running (bool)
assert gi.gi_running == False

# Test gi.gi_yieldfrom
gi.gi_yieldfrom = None
assert gi.gi_yieldfrom == None

# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals['x'] = 1
assert gi.gi_frame.f_locals['x'] == 1

# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno = 1
assert gi.gi_frame.f_
