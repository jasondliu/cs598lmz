gi = (i for i in ())
# Test gi.gi_code is NULL.
# Note: gi.gi_code is a macro and not a field in Python 3.
try:
    gi.gi_code
except AttributeError:
    pass
else:
    assert False, 'gi.gi_code is not NULL'

# Test gi.gi_frame is NULL.
# Note: gi.gi_frame is a macro and not a field in Python 3.
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    assert False, 'gi.gi_frame is not NULL'

# Test gi.gi_running is 0.
# Note: gi.gi_running is a macro and not a field in Python 3.
try:
    gi.gi_running
except AttributeError:
    pass
else:
    assert gi.gi_running == 0, 'gi.gi_running is not 0'

# Test gi.gi_yieldfrom is NULL.
# Note: gi.gi_yieldfrom is a macro and not a field in Python 3.
try:

