gi = (i for i in ())
# Test gi.gi_code is None
g = gi.gi_frame.f_code
assert g.co_code is None
assert g.co_filename == '<string>'
assert g.co_name == '<genexpr>'
assert g.co_firstlineno == 1
assert g.co_lnotab == b''
assert g.co_stacksize == 0
assert g.co_flags == 0x00000040
assert g.co_consts == (None, '<genexpr>')
assert g.co_names == ()
assert g.co_varnames == ()
assert g.co_freevars == ()
assert g.co_cellvars == ()

# Test gi.gi_frame.f_lasti is -1
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}

# Test gi.gi_frame.f_trace is None
assert gi.gi_frame.f_trace is None

# Test
