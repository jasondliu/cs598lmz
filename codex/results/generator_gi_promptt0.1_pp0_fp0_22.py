gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send
print(gi.send(None))
# Test gi.throw
print(gi.throw(StopIteration))
# Test gi.close
print(gi.close())
# Test gi.__next__
print(gi.__next__())
# Test gi.__iter__
print(gi.__iter__())
# Test gi.__await__
print(gi.__await__())
# Test gi.async_code
print(gi.async_code)
# Test gi.async_gen
print(gi.async_gen)
# Test gi.async_gen_hooks
print(gi.async_gen_hooks)
# Test gi.async_gen_finalizer
print(gi.
