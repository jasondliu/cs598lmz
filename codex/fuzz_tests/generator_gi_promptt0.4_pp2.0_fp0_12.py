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

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError expected here')

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError expected here')

# Test gi.send(None)
try:
    gi.send(None)
except TypeError:
    pass
else:
    print('TypeError expected here')

# Test gi.throw(None)
try:
    gi.throw(None)
except TypeError:
    pass
else:
    print('TypeError expected here')

# Test gi.
