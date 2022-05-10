gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.__next__
gi.__next__()
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()

# Test gi.__reduce__
gi.__reduce__()
# Test gi.__reduce_ex__
gi.__reduce_ex__(2)

# Test gi.__await__
gi.__await__()
# Test gi.async_gen
gi.async_gen
# Test gi.async_gen.ag_await
gi.async_gen.ag_await
# Test gi.async_gen.ag_frame
gi.async_gen.ag_frame
# Test gi.async_gen.
