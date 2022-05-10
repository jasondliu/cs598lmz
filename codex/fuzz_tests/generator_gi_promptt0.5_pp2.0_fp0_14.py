gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_varnames
print(gi.gi_frame.f_code.co_varnames)

# Test gi.gi_code.co_varnames
try:
    print(gi.gi_code.co_varnames)
except AttributeError:
    print("AttributeError")

# Test gi.gi_frame.f_code.co_argcount
print(gi.gi_frame.f_code.co_argcount)

# Test gi.gi_code.co_argcount
try:
    print(gi.gi_code.co_argcount)
except AttributeError:
    print("AttributeError")

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_
