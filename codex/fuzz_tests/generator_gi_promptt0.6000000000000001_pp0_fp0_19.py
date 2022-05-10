gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame and gi.gi_running
# Can't use gi.gi_frame --- it's not a real attribute
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise TestFailed, 'gi.gi_code should not exist'
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    raise TestFailed, 'gi.gi_frame should not exist'
try:
    gi.gi_running
except AttributeError:
    pass
else:
    raise TestFailed, 'gi.gi_running should not exist'

gi = (i for i in (1,2,3))
# Test gi.gi_code, gi.gi_frame and gi.gi_running
# Can't use gi.gi_frame --- it's not a real attribute
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise TestFailed, 'gi.gi_code should not exist'
try:
    g
