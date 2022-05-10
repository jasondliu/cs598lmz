gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code

# Test gi.gi_frame is None
gi.gi_frame

# Test gi.gi_running is 0
gi.gi_running

# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom

# Test gi.gi_weakreflist is None
gi.gi_weakreflist

# Test gi.__name__ is 'generator'
gi.__name__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__module__ is '__main__'
gi.__module__

# Test gi.__annotations__ is {}
gi.__annotations__

# Test gi.__dict__ is {}
gi.__dict__

# Test gi.__class__ is <class 'generator'>
gi.__class__

# Test gi.__await__() raises TypeError
try:
    gi.__await__()
except TypeError:
    pass
