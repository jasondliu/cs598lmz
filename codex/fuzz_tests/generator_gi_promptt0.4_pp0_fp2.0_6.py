gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & 0x20 == 0x20
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_trace
def trace_func(frame, event, arg):
    return trace_func
def f():
    pass
gi = (i for i in ())
gi.gi_frame.f_trace = trace_func
assert gi.gi_frame.f_trace(gi.gi_frame, 'call', None) is trace_func

# Test gi.gi_frame.f_trace_lines
def trace_func(frame, event, arg):
    return trace_func
def f():
    pass
gi = (i for i in ())
gi.gi_frame.f_trace_lines = trace_func
assert gi.gi_frame.f_trace_lines(gi.gi_frame, 'call', None) is trace_func

# Test gi.gi_frame.f_trace_
