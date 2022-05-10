gi = (i for i in ())
# Test gi.gi_code.co_flags
gi.gi_code.co_flags
# Test gi.gi_frame.f_code.co_flags
gi.gi_frame.f_code.co_flags
gi.gi_frame.f_code.co_flags = 0
# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals
gi.gi_frame.f_locals = {}
# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace
gi.gi_frame.f_trace = None
# Test gi.gi_running
gi.gi_running
gi.gi_running = False
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
gi.gi_yieldfrom = None

# Test gi.__await__
gi.__await__()
# Test gi.__aiter__
gi.__aiter__()
# Test gi.__anext__
gi.__anext__()
# Test gi.throw
gi.throw(Exception)
