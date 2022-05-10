gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x20

# Test gi.gi_frame
assert gi.gi_frame is None

# Test gi.gi_running
assert gi.gi_running is False

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.__name__
assert gi.__name__ == '<genexpr>'

# Test gi.__qualname__
assert gi.__qualname__ == '<genexpr>'

# Test gi.__module__
assert gi.__module__ == '__main__'

# Test gi.__class__
assert gi.__class__ is type(gi)

# Test gi.__await__
assert gi.__await__() is gi

# Test gi.__iter__
assert gi.__iter__() is gi

# Test gi.__next__
try:
    gi.__next__()
except StopIter
