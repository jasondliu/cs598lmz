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
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()
# Test gi.__iter__
gi.__iter__()
# Test gi.async_code
gi.async_code
# Test gi.async_gen
gi.async_gen
# Test gi.async_gen.aclose
gi.async_gen.aclose()
# Test gi.async_gen.asend
gi.async_gen.asend(None)
# Test gi.async_gen.athrow
gi.async_gen.athrow(StopIteration)
# Test gi.async_gen.ag_aw
