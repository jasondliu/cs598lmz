gi = (i for i in ())
# Test gi.gi_code is None
try:
    exec(gi)
except ValueError:
    pass
else:
    raise TestFailed("exec(gi) didn't raise ValueError")

# Test that gi.gi_frame is None
gi.gi_frame

# Test gi.gi_running is 0
gi.gi_running


# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom

# Test gi.__name__ is '<genexpr>'
gi.__name__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__qualname__ is '<genexpr>'
gi.__qualname__

# Test gi.__qual
