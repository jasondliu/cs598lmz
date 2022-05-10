gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
    gi.gi_code = 2
    print('AttributeError expected')
except AttributeError:
    pass

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
    gi.gi_frame = 2
    print('AttributeError expected')
except AttributeError:
    pass

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
    gi.gi_running = 2
    print('AttributeError expected')
except AttributeError:
    pass

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
