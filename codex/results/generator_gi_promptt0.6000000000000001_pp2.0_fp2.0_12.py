gi = (i for i in ())
# Test gi.gi_code is None.
try:
    gi.gi_code
except AttributeError:
    print('AttributeError')

# Test gi.gi_frame is None.
try:
    gi.gi_frame
except AttributeError:
    print('AttributeError')
