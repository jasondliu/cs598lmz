gi = (i for i in ())
# Test gi.gi_code.
TestError(TypeError, gi.gi_code)
TestError(TypeError, gi.gi_code.co_name)
TestError(TypeError, gi.gi_code.co_filename)
