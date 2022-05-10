gi = (i for i in ())
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<stdin>'

# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<stdin>'

s = iter(())
# Test s.gi_code.co_filename
assert s.gi_code.co_filename == '<stdin>'

# Test s.gi_frame.f_code.co_filename
assert s.gi_frame.f_code.co_filename == '<stdin>'
