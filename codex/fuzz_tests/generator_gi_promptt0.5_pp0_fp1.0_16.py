gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('FAILED: gi.gi_code is not None')
# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('FAILED: gi.gi_frame is not None')

# Test that gi.gi_frame.f_code is None
try:
    gi.gi_frame.f_code
except AttributeError:
    pass
else:
    print('FAILED: gi.gi_frame.f_code is not None')

# Test that gi.gi_frame.f_lasti is None
try:
    gi.gi_frame.f_lasti
except AttributeError:
    pass
else:
    print('FAILED: gi.gi_frame.f_lasti is not None')

# Test that gi.gi_frame.f_lineno is None
try:
    gi
