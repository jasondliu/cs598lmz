gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('FAILED')

# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('FAILED')

# Test gi.gi_running is True
try:
    gi.gi_running
except AttributeError:
    print('FAILED')
else:
    if not gi.gi_running:
        print('FAILED')

# gi.gi_running is True
# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('FAILED')

# Test gi.gi_code is not None
try:
    gi.gi_code
except AttributeError:
    print('FAILED')
else:
    if gi.gi_code is None:
        print('FAILED')

# gi.
