gi = (i for i in ())
# Test gi.gi_code.co_name attribute.
print(gi.gi_code.co_name)
# Test gi.gi_frame.f_code.co_name attribute.
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_frame.f_code.co_filename attribute.
print(gi.gi_frame.f_code.co_filename)
# Test gi.gi_running attribute.
print(gi.gi_running)

# Test gi.gi_frame.f_lineno attribute.
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti attribute.
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_trace attribute.
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace_lines attribute.
print(gi.gi_frame.f_trace_lines)

# Test gi.gi_frame.f_trace_opcodes attribute.

