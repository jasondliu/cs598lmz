gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == (CO_GENERATOR | CO_ITERABLE_COROUTINE)
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_code.co_flags
assert gi.gi_frame.f_code.co_flags == (CO_GENERATOR | CO_ITERABLE_COROUTINE)
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<genexpr>'

# Test gi.gi_frame.f_code.co_names
assert gi.gi_frame.f_code.co_names == ('range',)
# Test gi.gi_frame.f_code.co_varnames
assert gi.gi_frame.f_code.co_varnames == ('i',)

# Test gi.gi_frame.f_back
assert gi
