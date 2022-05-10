gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.__name__
print(gi.__name__)

# Test gi.__qualname__
print(gi.__qualname__)

# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)
# Test gi.gi_frame.f_builtins
print(gi.gi_frame.f_builtins)
# Test gi.gi_frame.f_code
print(gi.gi_frame.f_code)
# Test gi.gi_frame.f_globals
print(gi.gi_frame.
