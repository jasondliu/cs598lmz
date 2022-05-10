gi = (i for i in ())
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == "<string>"

# Test gi.gi_code.co_name
assert gi.gi_code.co_name == "<genexpr>"

# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == "<string>"

# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == "<module>"

# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {"gi": gi}

# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 1
