gi = (i for i in ())
# Test gi.gi_code is None
print('gi.gi_code is', gi.gi_code)
# Test gi.gi_frame is None
print('gi.gi_frame is', gi.gi_frame)

# Test gi.gi_running is False
print('gi.gi_running is', gi.gi_running)
# Test gi.gi_frame.f_lasti is None
print('gi.gi_frame.f_lasti is', gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno is 0
print('gi.gi_frame.f_lineno is', gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_builtins is __builtin__
print('gi.gi_frame.f_builtins is', gi.gi_frame.f_builtins)

# Test gi.gi_frame.f_globals is __main__
print('gi.gi_frame.f_globals is', gi.gi_frame.f_
