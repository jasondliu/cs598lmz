gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.__name__
print(gi.__name__)
# Test gi.__qualname__
print(gi.__qualname__)
# Test gi.__annotations__
print(gi.__annotations__)
# Test gi.__await__
print(gi.__await__())
# Test gi.__aiter__
print(gi.__aiter__())
# Test gi.__anext__
print(gi.__anext
