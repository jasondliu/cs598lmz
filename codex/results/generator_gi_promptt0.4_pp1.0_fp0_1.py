gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

try:
    gi.gi_code = 3
except TypeError:
    print('TypeError')

# Test gi.gi_frame
gi.gi_frame

try:
    gi.gi_frame = 3
except TypeError:
    print('TypeError')

# Test gi.gi_running
gi.gi_running

try:
    gi.gi_running = 3
except TypeError:
    print('TypeError')

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

try:
    gi.gi_yieldfrom = 3
except TypeError:
    print('TypeError')
