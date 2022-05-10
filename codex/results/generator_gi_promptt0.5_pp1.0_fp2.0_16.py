gi = (i for i in ())
# Test gi.gi_code.
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_code.co_filename == '<stdin>'
assert gi.gi_code.co_firstlineno == 1
assert gi.gi_code.co_flags == 67
assert gi.gi_code.co_consts == (None,)
assert gi.gi_code.co_names == ()
assert gi.gi_code.co_varnames == ()
assert gi.gi_code.co_freevars == ()
assert gi.gi_code.co_cellvars == ()

def f(x):
    y = x * 2
    yield y

gi = f(1)
# Test gi.gi_code.
assert gi.gi_code.co_name == 'f'
assert gi.gi_code.co_filename == '<stdin>'
assert gi.gi_code.co_firstlineno == 1
assert gi.gi_code.co_flags == 67
assert gi.gi
