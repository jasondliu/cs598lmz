gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x20

# Test gi.gi_code.co_code
assert gi.gi_code.co_code == b''

# Test gi.gi_code.co_consts
assert gi.gi_code.co_consts == (None,)

# Test gi.gi_code.co_names
assert gi.gi_code.co_names == ()

# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()

# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<stdin>'

# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'

# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 1

# Test gi.gi_code.co_lnotab
