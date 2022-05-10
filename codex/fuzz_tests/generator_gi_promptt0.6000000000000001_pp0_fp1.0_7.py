gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 0
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == ''
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_code.co_firstlineno
assert gi.gi_frame.f_code.co_firstlineno == 0
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == ''
# Test gi.gi_frame.f_code.co_varnames
assert gi.gi_frame.f_code.co_varnames == ()
# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}

#
