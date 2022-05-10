gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_locals is gi.gi_frame.f_locals
print(gi.gi_frame.f_locals is gi.gi_frame.f_locals)
# Test gi.gi_frame.f_locals is not gi.gi_frame.f_locals
print(gi.gi_frame.f_locals is not gi.gi_frame.f_locals)
# Test gi.gi_frame.f_locals is not gi.gi_frame.f_locals
print(gi.gi_frame.f_locals is not gi.gi_frame.f_locals)
# Test gi.gi_frame.f_locals is not gi.gi_frame.f_locals
print(gi.gi_frame.f_locals is not gi.gi_frame.f
