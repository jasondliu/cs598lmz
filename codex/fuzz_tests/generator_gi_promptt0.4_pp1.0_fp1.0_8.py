gi = (i for i in ())
# Test gi.gi_code is None.
gi.gi_code

# Test gi.gi_frame is None.
gi.gi_frame

# Test gi.gi_running is False.
gi.gi_running

# Test gi.gi_yieldfrom is None.
gi.gi_yieldfrom

# Test gi.send() raises TypeError.
try:
    gi.send(None)
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")

# Test gi.throw() raises TypeError.
try:
    gi.throw(None)
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")

# Test gi.close() raises TypeError.
try:
    gi.close()
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")

# Test gi.__next__() raises TypeError.
try:
    next(gi)
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")
