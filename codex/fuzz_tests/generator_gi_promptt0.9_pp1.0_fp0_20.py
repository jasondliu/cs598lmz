gi = (i for i in ())
# Test gi.gi_code.
try:
    gi.gi_code
except AttributeError:
    print('AttributeError')
# Test gi.gi_frame.
try:
    gi.gi_frame
except AttributeError:
    print('AttributeError')
# Test gi.gi_running.
try:
    gi.gi_running
except AttributeError:
    print('AttributeError')
# Test gi.gi_yieldfrom.
try:
    gi.gi_yieldfrom
except Attri
