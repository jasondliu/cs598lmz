gi = (i for i in ())
# Test gi.gi_code
gi.gi_code # CodeType #

# Test gi.gi_frame
gi.gi_frame # FrameType #

# Test gi.gi_running
gi.gi_running # bool #

# Test gi.gi_yieldfrom
gi.gi_yieldfrom # object #

# Test gi.gi_name
gi.gi_name # str #

# Test gi.gi_qualname
gi.gi_qualname # str #

# Test gi.send
gi.send(None) # object #

# Test gi.throw
gi.throw(None) # object #

# Test gi.close
gi.close() # None #

# Test gi.__next__
gi.__next__() # object #

# Test gi.__iter__
gi.__iter__() # object #

# Test gi.send
gi.send(None) # object #

# Test gi.throw
gi.throw(None) # object #

# Test gi.close
gi.close() # None
