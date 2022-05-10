gi = (i for i in ())
# Test gi.gi_code is unused
gi.gi_code
# Compile gi's frame
execute_code(gi.gi_frame.f_code, gi.gi_frame.f_globals, gi.gi_frame.f_locals, gi.gi_frame)
# Test gi.gi_code is used
gi.gi_code
