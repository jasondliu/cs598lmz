gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_trace
def trace(frame, event, arg):
    print(frame.f_lineno, event)

gi.gi_frame.f_trace = trace

# Test gi.gi_frame.f_trace_lines
gi.gi_frame.f_trace_lines = True

# Test gi.gi_frame.f_trace_opcodes
gi.gi_frame.f_trace_opcodes = True

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)

# Test gi
