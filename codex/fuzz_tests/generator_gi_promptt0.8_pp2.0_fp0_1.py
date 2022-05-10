gi = (i for i in ())
# Test gi.gi_code
gi.gi_code.co_varnames
gi.gi_code.co_argcount
# Test gi.gi_frame with a callable
def f():
    gi.gi_frame.f_locals
    gi.gi_frame.f_globals
    # Test gi.gi_frame.f_code.co_varnames
    gi.gi_frame.f_code.co_varnames

f()
# Test gi.gi_frame with a non-callable
gi.gi_frame.f_locals

gi.gi_frame.f_globals
gi.gi_frame.f_code.co_varnames
