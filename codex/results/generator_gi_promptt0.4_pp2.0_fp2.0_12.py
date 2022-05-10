gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x0000
# Test gi.gi_code.co_code
assert gi.gi_code.co_code == b''
# Test gi.gi_code.co_consts
assert gi.gi_code.co_consts == (None,)
# Test gi.gi_code.co_names
assert gi.gi_code.co_names == ()
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()
# Test gi.gi_code.co_freevars
assert gi.gi_code.co_freevars == ()
# Test gi.gi_code.co_cellvars
assert gi.gi_code.co_cellvars == ()
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<string>'
# Test gi.gi_code.co_name
assert gi.gi_code.co_name
