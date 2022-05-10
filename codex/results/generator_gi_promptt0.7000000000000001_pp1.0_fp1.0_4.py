gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x21)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

gi.gi_frame.f_lasti = 42
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace_lines
print(gi.gi_frame.f_trace_lines)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
