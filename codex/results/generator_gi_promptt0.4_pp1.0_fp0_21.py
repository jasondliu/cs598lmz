gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame
print(gi.gi_code, gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace = None
gi.gi_frame.f_trace = None
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace = sys.gettrace()
gi.gi_frame.f_trace = sys.gettrace()
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace = sys
