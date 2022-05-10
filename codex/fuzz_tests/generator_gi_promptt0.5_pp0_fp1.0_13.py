gi = (i for i in ())
# Test gi.gi_code.co_varnames
print(gi.gi_code.co_varnames)
# Test gi.gi_code.co_argcount
print(gi.gi_code.co_argcount)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_globals
print(gi.gi_frame.f_globals)
