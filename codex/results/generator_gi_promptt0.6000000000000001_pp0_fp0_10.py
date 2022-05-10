gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code should raise AttributeError")
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_frame should raise AttributeError")
# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_running should raise AttributeError")
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_yieldfrom should raise AttributeError")

if sys.version_info[:2] < (3, 7):
    # Make sure that gi.send() raises a TypeError
    try:
        gi.send(None)
    except TypeError:
        pass
    else
