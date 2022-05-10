gi = (i for i in ())
# Test gi.gi_code.co_filename
print(gi.gi_code.co_filename)

print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_filename
# print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_globals['__name__']
print(gi.gi_frame.f_globals['__name__'])

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f
