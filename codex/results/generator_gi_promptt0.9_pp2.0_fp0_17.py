gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_code)

# Test gi.gi_code.co_freevars
print(gi.gi_code.co_freevars)

# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_code
print(gi.gi_frame.f_code.co_code)

# Test gi.gi_frame.f_code.co_freevars
print(gi.gi_frame.f_code.co_freevars)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)
