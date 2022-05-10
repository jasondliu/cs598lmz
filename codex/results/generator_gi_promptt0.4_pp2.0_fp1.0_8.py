gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)

# Test gi.gi_frame is None
print(gi.gi_frame)

# Test gi.gi_running is False
print(gi.gi_running)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.__class__ is GeneratorType
print(gi.__class__ is GeneratorType)

# Test gi.__name__ is '<genexpr>'
print(gi.__name__)

# Test gi.__qualname__ is '<genexpr>'
print(gi.__qualname__)

# Test gi.gi_frame.f_code.co_name is '<genexpr>'
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename is '<dis>'
print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.
