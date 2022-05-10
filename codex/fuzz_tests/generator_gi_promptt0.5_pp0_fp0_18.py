gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise RuntimeError("gi.gi_code should be None")

# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    raise RuntimeError("gi.gi_frame should be None")

# Test gi.gi_running is False
gi.gi_running

# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom

# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom

# Test gi.gi_name is '<genexpr>'
gi.gi_name

# Test gi.gi_qualname is '<genexpr>'
gi.gi_qualname

# Test gi.gi_exc_state is None
gi.gi_exc_state

# Test gi.gi_weakreflist is []
gi.gi_weakreflist

# Test gi.gi_
