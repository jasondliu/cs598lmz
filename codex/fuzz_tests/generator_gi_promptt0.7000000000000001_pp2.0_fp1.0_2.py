gi = (i for i in ())
# Test gi.gi_code
gi.gi_code is None
# Test gi.gi_frame
gi.gi_frame is None
# Test gi.gi_running
gi.gi_running == 0
# Test gi.gi_yieldfrom
gi.gi_yieldfrom is None
# Test gi.gi_name
gi.gi_name is None
# Test gi.gi_qualname
gi.gi_qualname is None

# Test gi.send
try:
    gi.send(None)
except TypeError:
    pass
else:
    raise Exception('Expected exception not raised')

# Test gi.send
try:
    gi.throw(None)
except TypeError:
    pass
else:
    raise Exception('Expected exception not raised')

# Test gi.send
try:
    gi.close()
except TypeError:
    pass
else:
    raise Exception('Expected exception not raised')

# Test gi.send
try:
    next(gi)
except StopIteration:
    pass
else:
    raise
