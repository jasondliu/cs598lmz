gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.__code__
try:
    gi.__code__
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.__frame__
try:
    gi.__frame__
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.__running__
try:
    gi.__running__
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test gi.gi_yieldfrom

