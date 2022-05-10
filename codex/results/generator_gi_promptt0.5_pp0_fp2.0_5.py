gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & CO_FUTURE_GENERATOR_STOP

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno

# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace

# Test gi.gi_frame.f_trace_lines
gi.gi_frame.f_trace_lines

# Test gi.gi_frame.f_trace_opcodes
gi.gi_frame.f_trace_opcodes

# Test gi.gi_frame.f_code.co_flags
gi.gi_frame.f_code.co_flags

# Test gi.gi_frame.f_code.co_lnotab
gi.gi_frame.f_code.co_lnotab

# Test gi.gi_frame.f_code.co_firstlineno
gi.gi
