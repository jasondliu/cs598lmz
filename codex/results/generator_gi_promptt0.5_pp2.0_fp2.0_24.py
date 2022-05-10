gi = (i for i in ())
# Test gi.gi_code.co_freevars
print(gi.gi_code.co_freevars)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_locals['i']
print(gi.gi_frame.f_locals['i'])
print(gi.gi_frame.f_locals['i'].gi_frame.f_locals)

# Test gi.gi_frame.f_locals['i'].gi_frame.f_locals['i']
print(gi.gi_frame.f_locals['i'].gi_frame.f_locals['i'])
print(gi.gi_frame.f_locals['i'].gi_frame.f_locals['i'].gi_frame.f_locals)

# Test gi.gi_frame.f_locals['i'].gi_frame.f_locals['i'].gi_frame.f_locals['i']
print(gi.
