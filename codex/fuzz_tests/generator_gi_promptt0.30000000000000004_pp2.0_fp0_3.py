gi = (i for i in ())
# Test gi.gi_code is None.
gi.gi_code

# Test gi.gi_frame is None.
gi.gi_frame

# Test gi.gi_running is False.
gi.gi_running

# Test gi.gi_yieldfrom is None.
gi.gi_yieldfrom

# Test gi.__name__ is None.
gi.__name__

# Test gi.__qualname__ is None.
gi.__qualname__

# Test gi.__module__ is None.
gi.__module__

# Test gi.__annotations__ is empty.
gi.__annotations__

# Test gi.__dict__ is empty.
gi.__dict__

# Test gi.__class__ is generator.
gi.__class__

# Test gi.__await__() is a coroutine.
gi.__await__()

# Test gi.send() raises TypeError.
try:
    gi.send(1)
except TypeError:
    pass
else:
    raise RuntimeError

