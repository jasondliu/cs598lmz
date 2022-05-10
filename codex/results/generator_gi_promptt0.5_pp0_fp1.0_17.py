gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None

# Test gi.gi_frame
assert gi.gi_frame is None

# Test gi.gi_running
assert gi.gi_running is False

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.__name__
assert gi.__name__ is None

# Test gi.__qualname__
assert gi.__qualname__ is None

# Test gi.__module__
assert gi.__module__ is None

# Test gi.__class__
assert gi.__class__ is type(gi)

# Test gi.__dict__
assert gi.__dict__ is {}

# Test gi.__setstate__
gi.__setstate__(None)

# Test gi.__reduce__
assert gi.__reduce__() == (type(gi), ())

# Test gi.__reduce_ex__
assert gi.__reduce_ex__(0)
