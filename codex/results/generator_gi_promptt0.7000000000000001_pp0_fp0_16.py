gi = (i for i in ())
# Test gi.gi_code == gi.gi_frame.f_code
assert gi.gi_code is gi.gi_frame.f_code
# Test gi.gi_code.co_flags == gi.gi_frame.f_code.co_flags
assert gi.gi_code.co_flags == gi.gi_frame.f_code.co_flags


def raise_exception(arg):
    # Test gi.gi_code == gi.gi_frame.f_code
    assert gi.gi_code is gi.gi_frame.f_code
    # Test gi.gi_code.co_flags == gi.gi_frame.f_code.co_flags
    assert gi.gi_code.co_flags == gi.gi_frame.f_code.co_flags
    raise arg

try:
    raise_exception(Exception())
except Exception as e:
    # Test gi.gi_code == gi.gi_frame.f_code
    assert gi.gi_code is gi.gi_frame.f
