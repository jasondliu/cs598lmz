gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected here')

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected here')
