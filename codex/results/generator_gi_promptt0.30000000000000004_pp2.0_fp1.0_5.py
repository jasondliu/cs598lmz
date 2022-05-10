gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x0000

# Test gi.gi_code.co_names
assert gi.gi_code.co_names == ()

# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()

# Test gi.gi_code.co_consts
assert gi.gi_code.co_consts == (None,)

# Test gi.gi_code.co_cellvars
assert gi.gi_code.co_cellvars == ()

# Test gi.gi_code.co_freevars
assert gi.gi_code.co_freevars == ()

# Test gi.gi_code.co_stacksize
assert gi.gi_code.co_stacksize == 1

# Test gi.gi_code.co_lnotab
assert gi.gi_code.co_lnotab == b''

# Test gi.gi_code.co_first
