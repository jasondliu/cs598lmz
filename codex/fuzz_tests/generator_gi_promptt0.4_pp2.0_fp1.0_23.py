gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code is None)

# Test gi.gi_frame is None
print(gi.gi_frame is None)

# Test gi.gi_running is False
print(gi.gi_running is False)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom is None)

# Test gi.__name__ is '<genexpr>'
print(gi.__name__ == '<genexpr>')

# Test gi.__qualname__ is '<genexpr>'
print(gi.__qualname__ == '<genexpr>')

# Test gi.__module__ is '__main__'
print(gi.__module__ == '__main__')

# Test gi.__class__ is generator
print(gi.__class__ is generator)

# Test gi.__dict__ is {}
print(gi.__dict__ == {})

# Test gi.__next__() raises StopIteration
try:
    gi.__next__()
