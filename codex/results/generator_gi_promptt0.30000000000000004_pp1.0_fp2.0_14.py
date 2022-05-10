gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 2
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 2
# Test gi.gi_frame.f_trace
assert gi.gi_frame.f_trace is None
# Test gi.gi_frame.f_trace_lines
assert gi.gi_frame.f_trace_lines is False
# Test gi.gi_frame.f_trace_opcodes
assert gi.gi_frame.f_trace_opcodes is False
# Test gi.gi_running
assert gi.gi_running is False
# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None
# Test gi.send(None)
assert next(gi) is None
# Test gi.send(1)
try:
    gi.send(1)

