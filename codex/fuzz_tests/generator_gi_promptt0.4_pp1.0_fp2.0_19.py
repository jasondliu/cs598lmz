gi = (i for i in ())
# Test gi.gi_code.co_varnames
print(gi.gi_code.co_varnames)
print(gi.gi_code.co_argcount)

# Test gi.gi_frame.f_code.co_varnames
print(gi.gi_frame.f_code.co_varnames)
print(gi.gi_frame.f_code.co_argcount)

# Test gi.gi_frame.f_locals.keys()
print(gi.gi_frame.f_locals.keys())
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_globals.keys()
print(gi.gi_frame.f_globals.keys())
print(gi.gi_frame.f_globals)

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)

# Test gi.gi_frame.f_back.f_locals.keys()
print(gi.gi_frame.f_back.f_
