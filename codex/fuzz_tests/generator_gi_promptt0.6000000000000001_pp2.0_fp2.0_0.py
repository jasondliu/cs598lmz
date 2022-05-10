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

# Test gi.send
try:
    gi.send('abc')
except TypeError:
    pass
else:
    print('TypeError expected')

# Test gi.throw
try:
    gi.throw(NameError, NameError('test'), None)
except NameError:
    pass
else:
    print('NameError expected')

# Test gi.close
try:
