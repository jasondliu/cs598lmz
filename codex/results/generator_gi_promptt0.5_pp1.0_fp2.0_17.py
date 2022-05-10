gi = (i for i in ())
# Test gi.gi_code.co_flags
test_gi_flags(gi, CO_GENERATOR)
# Test gi.gi_frame.f_lasti
test_gi_frame_lasti(gi, -1)
# Test gi.gi_frame.f_code.co_flags
test_gi_frame_flags(gi, CO_GENERATOR)
# Test gi.gi_frame.f_code.co_name
test_gi_frame_name(gi, '<genexpr>')

# Test generator expression
gi = (i for i in range(3))
# Test gi.gi_code.co_flags
test_gi_flags(gi, CO_GENERATOR)
# Test gi.gi_frame.f_lasti
test_gi_frame_lasti(gi, -1)
# Test gi.gi_frame.f_code.co_flags
test_gi_frame_flags(gi, CO_GENERATOR)
# Test gi.gi_frame.f_code.co_name
test_gi_frame_name(gi, '<
