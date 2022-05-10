gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_filename)
# Test gi.gi_frame.f_builtins.__new__
print(gi.gi_frame.f_builtins.__new__.__name__)
