gi = (i for i in ())
# Test gi.gi_code.co_flags
print(next(gi).gi_code.co_flags)
# Test gi.gi_frame.f_lasti
print(next(gi).gi_frame.f_lasti)
# Test gi.gi_frame.f_locals
print(next(gi).gi_frame.f_locals)
# Test gi.gi_frame.f_trace
print(next(gi).gi_frame.f_trace)
# Test gi.gi_running
print(next(gi).gi_running)
# Test gi.gi_yieldfrom
print(next(gi).gi_yieldfrom)
