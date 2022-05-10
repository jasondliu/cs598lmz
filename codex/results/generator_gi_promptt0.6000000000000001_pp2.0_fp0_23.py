gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)

# Test gi.gi_frame
print(gi.gi_frame)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_locals is gi.gi_frame.f_locals
print(gi.gi_frame.f_locals is gi.gi_frame.f_locals)

# Test gi.gi_frame.f_locals['i']
print(gi.gi_frame.f_locals['i'])

# Test gi.gi_frame.f_locals['i'] is gi.gi_frame.f_locals['i']
print(gi.gi_frame.f_locals['i'] is gi.gi_frame.f_locals['i'])

# Test gi.gi_frame.f_locals['i']
