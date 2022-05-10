gi = (i for i in ())
# Test gi.gi_code is a function object
print(gi.gi_code)
print(gi.gi_frame)
print(gi.gi_running)
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_code.co_name)
print(gi.gi_frame.f_code.co_varnames)
print(gi.gi_frame.f_code.co_argcount)

print(gi.gi_code.co_name)
print(gi.gi_code.co_varnames)
print(gi.gi_code.co_argcount)
print(gi.gi_code.co_nlocals)
print(gi.gi_code.co_stacksize)

# Test gi.gi_frame is None
gi = (i for i in range(5))
print(gi.gi_frame)

# Test gi.gi_running is False
gi.close()
print(gi.gi_running)

# Test gi.gi_frame.f_lasti is a number
gi = (i for
