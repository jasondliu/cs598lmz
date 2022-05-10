gi = (i for i in ())
# Test gi.gi_code.co_name
try:
    gi.gi_code.co_name
except AttributeError as e:
    print(e)
    assert e.args[0] == "'generator' object has no attribute 'co_name'"
# Test gi.gi_frame.f_code.co_name
try:
    gi.gi_frame.f_code.co_name
except AttributeError as e:
    print(e)
    assert e.args[0] == "'generator' object has no attribute 'f_code'"
