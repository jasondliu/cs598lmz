gi = (i for i in ())
# Test gi.gi_code
gi.gi_code.co_varnames
gi.gi_code.co_argcount

gi = (i for i in range(10))
gi.gi_code.co_varnames
gi.gi_code.co_argcount

gi = (i for i in range(10) for x in range(10))
gi.gi_code.co_varnames
gi.gi_code.co_argcount

# Test gi.gi_frame
gi = (i for i in range(10))
gi.gi_frame.f_lasti

# Test gi_frame.f_locals
gi = (i for i in range(10))
gi.gi_frame.f_locals

# Test gi_frame.f_back
gi = (i for i in range(10))
gi.gi_frame.f_back

# Test gi_frame.f_builtins
gi = (i for i in range(10))
gi.gi_frame.f_builtins

# Test gi_frame.f_globals
