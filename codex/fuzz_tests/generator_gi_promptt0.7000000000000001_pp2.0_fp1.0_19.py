gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
    raise TestFailed, "gi.gi_code should fail"
except AttributeError:
    pass
# Test gi.gi_frame
try:
    gi.gi_frame
    raise TestFailed, "gi.gi_frame should fail"
except AttributeError:
    pass

# Test that gi.gi_frame throws ValueError for gi's with no frame
def nested():
    gi = (i for i in ())
    try:
        gi.gi_frame
        raise TestFailed, "gi.gi_frame should fail"
    except ValueError, e:
        pass
nested()

# Test that gi.gi_frame throws ValueError if the frame is gone
def nested():
    gi = (i for i in ())
    try:
        gi.gi_frame
        raise TestFailed, "gi.gi_frame should fail"
    except ValueError:
        pass
    return gi

gi = nested()

import gc
gc.collect()

try
