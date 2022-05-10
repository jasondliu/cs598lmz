gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
    print('Code:', gi.gi_code)
except AttributeError:
    print('gi.gi_code not accessible in Python 3.x')
# Test gi.gi_frame
try:
    gi.gi_frame
    print('Frame:', gi.gi_frame)
except AttributeError:
    print('gi.gi_frame is not accessible in Python 3.x')
