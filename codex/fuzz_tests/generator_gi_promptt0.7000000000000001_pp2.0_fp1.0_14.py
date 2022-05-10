gi = (i for i in ())
# Test gi.gi_code
print(type(gi.gi_code))
print(gi.gi_code.co_code)
print(type(gi.gi_code.co_code))
# Test gi.gi_frame
print(type(gi.gi_frame))
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_frame.f_locals
print(type(gi.gi_frame.f_locals))
print(gi.gi_frame.f_locals)
