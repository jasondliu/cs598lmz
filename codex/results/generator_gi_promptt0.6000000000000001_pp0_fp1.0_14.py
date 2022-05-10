gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
print(gi.gi_code.co_firstlineno)

# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_locals['i']
print(gi.gi_frame.f_locals['i'])
