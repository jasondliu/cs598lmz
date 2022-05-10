gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == "empty_gen"
assert gi.gi_code.co_filename == __file__
assert gi.gi_code.co_firstlineno == 4
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame
assert gi.gi_frame.f_back is None
assert gi.gi_frame.f_builtins is __builtins__
assert gi.gi_frame.f_code.co_name == "empty_gen"
assert gi.gi_frame.f_code.co_filename == __file__
assert gi.gi_frame.f_code.co_firstlineno == 4
assert gi.gi_frame.f_lasti == -1
assert gi.gi_frame.f_lineno == 4
assert gi.gi_frame.f_locals == {}
assert gi.gi_frame.f_trace is None

gi.gi_frame.f_trace = lambda f, e, o: None
assert gi.
