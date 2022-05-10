gi = (i for i in ())
# Test gi.gi_code.co_argcount
assert gi.gi_code.co_argcount == 0
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()
# Test gi.gi_code.co_cellvars
assert gi.gi_code.co_cellvars == ()
# Test gi.gi_code.co_freevars
assert gi.gi_code.co_freevars == ()
# Test gi.gi_code.co_nlocals
assert gi.gi_code.co_nlocals == 0
# Test gi.gi_code.co_stacksize
assert gi.gi_code.co_stacksize == 0
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x4

# Test gi.gi_code.co_code
assert gi.gi_code.co_code == b'|\x00|\x01\x17\x00'
# Test gi.gi
