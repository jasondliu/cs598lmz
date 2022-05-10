gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)

# Test gi.gi_frame.f_lasti
gi = (i for i in ())
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno
gi = (i for i in ())
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_trace
gi = (i for i in ())
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace_lines
gi = (i for i in ())
print(gi.gi_frame.f_trace_lines)

# Test gi.gi_frame.f_trace_opcodes
gi = (i for i in ())
print(gi.gi_frame.f_trace_opcodes)

# Test gi.gi_running
