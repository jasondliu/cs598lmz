gi = (i for i in ())
# Test gi.gi_code == None
try:
    gi.gi_code
except AttributeError:
    print('AttributeError')

# Test gi.gi_frame == None
try:
    gi.gi_frame
except AttributeError:
    print('AttributeError')

# Test gi.gi_running == 0
gi.gi_running = 42
print(gi.gi_running)

# Test gi.gi_yieldfrom == None
try:
    gi.gi_yieldfrom
except AttributeError:
    print('AttributeError')

try:
    gi.attr
except AttributeError:
    print('AttributeError')
