gi = (i for i in ())
# Test gi.gi_code is not None
print(gi.send(None))

# Test gi.gi_frame is not None
# print(gi.gi_frame.f_code.co_name)

# Test gi.gi_running is False
print(gi.gi_running)

# Test gi.gi_frame.f_lasti is not None
# print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_locals is not None
# print(gi.gi_frame.f_locals)
