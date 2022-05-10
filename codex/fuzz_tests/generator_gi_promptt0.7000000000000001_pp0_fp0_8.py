gi = (i for i in ())
# Test gi.gi_code.co_code
assert gi.gi_code.co_code == b'e'
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<input>'
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 1
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'test'
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<input>'
# Test gi.gi_frame.f_code.co_firstlineno
assert gi.gi_frame.f_code.co_firstlineno == 5
# Test gi.gi_frame.f_locals.__module__
assert gi.gi_
