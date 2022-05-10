gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.__name__
gi.__name__
# Test gi.__qualname__
gi.__qualname__
# Test gi.__next__
gi.__next__
# Test gi.__length_hint__
gi.__length_hint__

# Test gi.send
with raises(TypeError):
    gi.send(1)

# Test gi.throw
with raises(TypeError):
    gi.throw(1)

# Test gi.close
gi.close()

# Test gi.send
gi.send(None)

# Test gi.throw
gi.throw(StopIteration)

# Test gi.close
gi.close()

# Test gi.close
gi.close()
