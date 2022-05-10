gi = (i for i in ())
# Test gi.gi_code is the same as the function
assert gi.gi_code is my_func.__code__
# Test gi.gi_frame is a frame object with the right lineno
assert gi.gi_frame.f_lineno == 2
</code>

