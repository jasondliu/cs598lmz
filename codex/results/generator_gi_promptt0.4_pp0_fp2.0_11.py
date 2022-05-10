gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_trace
def trace_func(frame, event, arg):
    print(frame.f_code.co_name)
    return trace_func

gi.gi_frame.f_trace = trace_func
gi.gi_frame.f_trace(gi.gi_frame, 'line', None)

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)
