gi = (i for i in ())
# Test gi.gi_code.co_flags
print(next(gi).gi_code.co_flags)

# Test gi.gi_frame.f_lasti
print(next(gi).gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno
print(next(gi).gi_frame.f_lineno)

# Test gi.gi_running
print(next(gi).gi_running)

# Test gi.gi_frame.f_trace
print(next(gi).gi_frame.f_trace)

# Test gi.gi_frame.f_trace_lines
print(next(gi).gi_frame.f_trace_lines)

# Test gi.gi_frame.f_trace_opcodes
print(next(gi).gi_frame.f_trace_opcodes)

# Test gi.gi_frame.f_code.co_filename
print(next(gi).gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_name

