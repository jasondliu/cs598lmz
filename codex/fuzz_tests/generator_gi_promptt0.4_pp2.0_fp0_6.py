gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_code.co_code
print(gi.gi_code.co_code)
print(gi.gi_code.co_code == bytes([]))
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)
# Test gi.gi_frame.f_trace_lines
print(gi.gi_frame.f_trace_lines)
# Test gi.gi_frame.f_trace_opcodes
print(gi.gi_frame.f_trace_opcodes)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)
# Test gi.gi_frame.f_code.co_code
