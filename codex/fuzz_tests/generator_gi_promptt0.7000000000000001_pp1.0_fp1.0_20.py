gi = (i for i in ())
# Test gi.gi_code.co_argcount == 0
assert gi.gi_code.co_argcount == 0
# Test gi.gi_code.co_cellvars == ()
assert gi.gi_code.co_cellvars == ()
# Test gi.gi_code.co_code == b'd\x00\x00d\x01\x00S'
assert gi.gi_code.co_code == b'd\x00\x00d\x01\x00S'
# Test gi.gi_code.co_consts == (None, None)
assert gi.gi_code.co_consts == (None, None)
# Test gi.gi_code.co_filename == '<stdin>'
assert gi.gi_code.co_filename == '<stdin>'
# Test gi.gi_code.co_firstlineno == 1
assert gi.gi_code.co_firstlineno == 1
# Test gi.gi_code.co_flags == 67
assert gi.gi_code.co_flags ==
