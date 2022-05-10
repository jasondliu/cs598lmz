gi = (i for i in ())
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ('i',)

# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}

# Test gi.gi_frame.f_globals
assert gi.gi_frame.f_globals == {}

# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<stdin>'

# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'

# Test gi.gi_frame.f_code.co_firstlineno
assert gi.gi_frame.f_code.co_firstlineno == 1

# Test gi.gi_frame.f_code.co_argcount
assert gi.gi_frame.f_code.co_argcount == 0

# Test gi.gi_
