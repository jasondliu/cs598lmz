gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)

# Test gi.gi_frame is None
print(gi.gi_frame)

# Test gi.gi_running is 0
print(gi.gi_running)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.gi_weakreflist is None
print(gi.gi_weakreflist)

# Test gi.gi_name is '<genexpr>'
print(gi.gi_name)

# Test gi.gi_qualname is '<genexpr>'
print(gi.gi_qualname)

# Test gi.gi_frame.f_lasti is -1
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno is 1
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_code.co_name is '<genexpr>'
print(gi.gi_frame
