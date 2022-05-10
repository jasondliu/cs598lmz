gi = (i for i in ())
# Test gi.gi_code
# gi.gi_code is None

# Test gi.gi_frame
# gi.gi_frame is None

# Test gi.gi_running
# gi.gi_running is False

# Test gi.gi_yieldfrom
# gi.gi_yieldfrom is None

# Test gi.__name__
# gi.__name__ is None

# Test gi.__qualname__
# gi.__qualname__ is None

# Test gi.__module__
# gi.__module__ is None

# Test gi.__await__
# gi.__await__() is gi

# Test gi.__iter__
# gi.__iter__() is gi

# Test gi.__next__
# raises StopIteration
# gi.__next__()

# Test gi.send
# raises TypeError
# gi.send(None)

# Test gi.throw
# raises TypeError
# gi.throw(None)

# Test
