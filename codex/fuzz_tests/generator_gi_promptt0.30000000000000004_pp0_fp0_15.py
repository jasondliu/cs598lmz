gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_firstlineno
print(gi.gi_frame.f_code.co_firstlineno)

# Test gi.gi_frame.f_code.co_lnotab
print(gi.gi_frame.f_code.co_lnotab)

# Test gi.gi_frame.f_code.co_argcount
print(gi.gi_frame.f_code.co_argcount)

# Test gi.gi_frame.f_code.co
