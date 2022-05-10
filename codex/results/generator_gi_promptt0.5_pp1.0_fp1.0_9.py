gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.send
# gi.send(None)
# Test gi.throw
# gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()

# Test gi.send
gi = (i for i in ())
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()

# Test gi.send
gi = (i for i in ())
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()


