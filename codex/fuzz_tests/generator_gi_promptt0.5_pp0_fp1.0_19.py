gi = (i for i in ())
# Test gi.gi_code.co_flags (not defined for 3.1)
try:
    assert gi.gi_code.co_flags == 67
except AttributeError:
    pass

# Test gi.gi_frame
gi = (i for i in ())
gi.gi_frame = None
try:
    gi.gi_frame = None
except TypeError:
    pass

# Test gi.gi_frame.f_code
gi = (i for i in ())
assert gi.gi_frame.f_code == gi.gi_code
try:
    gi.gi_frame.f_code = None
except TypeError:
    pass

# Test gi.gi_frame.f_lasti
gi = (i for i in ())
assert gi.gi_frame.f_lasti == -1
try:
    gi.gi_frame.f_lasti = None
except TypeError:
    pass

# Test gi.gi_frame.f_lineno
gi = (i for i in ())
assert gi.gi_frame.f_
