gi = (i for i in ())
# Test gi.gi_code.co_varnames
gi.gi_code.co_varnames == ()
# Test gi.gi_frame.f_code.co_varnames
gi.gi_frame.f_code.co_varnames == ()

# Test __name__
gi.gi_name == ''
# Test __qualname__
gi.gi_qualname == ''

# Test gi.gi_code.co_argcount
gi.gi_code.co_argcount == 0
# Test gi.gi_frame.f_code.co_argcount
gi.gi_frame.f_code.co_argcount == 0

# Test gi.gi_code.co_argnames
gi.gi_code.co_argnames == ()
# Test gi.gi_frame.f_code.co_argnames
gi.gi_frame.f_code.co_argnames == ()

# Test gi.gi_code.co_posonlyargcount
gi.gi_code.co_posonlyargcount == 0
# Test gi.gi_frame
