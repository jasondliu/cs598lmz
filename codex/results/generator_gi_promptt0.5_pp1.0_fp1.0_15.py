gi = (i for i in ())
# Test gi.gi_code.co_name (should be '<genexpr>')
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_name (should be '<module>')
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_back.f_code.co_name (should be '<genexpr>')
print(gi.gi_frame.f_back.f_code.co_name)

# Test gi.gi_frame.f_back.f_back.f_code.co_name (should be '<module>')
print(gi.gi_frame.f_back.f_back.f_code.co_name)
