gi = (i for i in ())
# Test gi.gi_code
gi.gi_code is None
# Test gi.gi_frame
gi.gi_frame is None
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom is None
# Test gi.__name__
gi.__name__ is None
# Test gi.__qualname__
gi.__qualname__ is None
# Test gi.send
# gi.send(None)
# Test gi.throw
# gi.throw(None)
# Test gi.close
gi.close()
# Test gi.gi_frame
gi.gi_frame is None
# Test gi.gi_running
gi.gi_running

# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(None)

# Test gi.close
# gi.close()

# Test gi.gi_frame
gi.gi_frame is None
# Test gi.gi_running
gi.gi_running

# Test g
