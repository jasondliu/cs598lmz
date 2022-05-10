gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_name
gi.gi_name

# Test gi.gi_frame
gi.gi_frame

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
gi.
