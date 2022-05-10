gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_running is False
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_yieldfrom is None
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.__name__ is None
try:
    gi.__name__
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.__qualname__ is None
try:
    gi.__qualname__
except AttributeError:
    pass
else:
    print("AttributeError expected")
