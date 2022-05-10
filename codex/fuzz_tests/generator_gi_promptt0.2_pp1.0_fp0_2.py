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

# Test gi.gi_frame.f_lasti
try:
    gi.gi_frame.f_lasti
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_lineno
try:
    gi.gi_frame.f_lineno
except AttributeError:
    pass
else:
    print
