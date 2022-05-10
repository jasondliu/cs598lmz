gi = (i for i in ())
# Test gi.gi_code is a function
assert isinstance(gi.gi_code, types.FunctionType)
assert gi.gi_code.__name__ is "next"
# Test gi.gi_frame is NULL
assert gi.gi_frame is None
# Test gi.gi_frame.f_code is a function
try:
    gi.gi_frame.f_code
except AttributeError:
    pass
else:
    assert False

# Check generator expression evaluation without an expressi
