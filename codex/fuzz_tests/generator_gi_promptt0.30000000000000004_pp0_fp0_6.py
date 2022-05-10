gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'

# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'

# Test gi.gi_frame.f_back.f_code.co_name
assert gi.gi_frame.f_back.f_code.co_name == '<module>'

# Test gi.gi_frame.f_back.f_back.f_code.co_name
assert gi.gi_frame.f_back.f_back.f_code.co_name == '<module>'

# Test gi.gi_frame.f_back.f_back.f_back.f_code.co_name
assert gi.gi_frame.f_back.f_back.f_back.f_code.co_name == '<module>'

# Test gi.gi_frame.f_back.f_back.f_back.f
