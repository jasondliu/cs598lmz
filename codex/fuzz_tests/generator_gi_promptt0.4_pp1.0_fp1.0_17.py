gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_code.co_argcount == 0
assert gi.gi_code.co_varnames == ()
assert gi.gi_code.co_filename == __file__
assert gi.gi_code.co_firstlineno == 1
assert gi.gi_code.co_lnotab == b''
assert gi.gi_code.co_freevars == ()
assert gi.gi_code.co_cellvars == ()

# Test gi.gi_frame
assert gi.gi_frame.f_back is None
assert gi.gi_frame.f_code == gi.gi_code
assert gi.gi_frame.f_locals == {}
assert gi.gi_frame.f_globals == globals()

# Test gi.gi_running
assert gi.gi_running == False

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test
