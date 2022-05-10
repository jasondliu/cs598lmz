gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_code.co_filename == '<input>'

# Test gi.gi_frame
assert gi.gi_frame.f_lasti == -1
assert gi.gi_frame.f_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_filename == '<input>'

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

#
