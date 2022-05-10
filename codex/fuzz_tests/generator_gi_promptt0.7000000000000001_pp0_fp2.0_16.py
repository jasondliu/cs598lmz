gi = (i for i in ())
# Test gi.gi_code == None
print(gi.gi_code)
# Test gi.gi_frame == None
print(gi.gi_frame)
# Test gi.gi_running == False
print(gi.gi_running)
# Test gi.gi_yieldfrom == None
print(gi.gi_yieldfrom)
# Test gi.gi_frame.f_lasti == -1
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno == 1
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_trace == None
print(gi.gi_frame.f_trace)
# Test gi.gi_frame.f_trace_lines == False
print(gi.gi_frame.f_trace_lines)
# Test gi.gi_frame.f_trace_opcodes == False
print(gi.gi_frame.f_trace_opcodes)
# Test gi.gi_frame.f_builtins == {}
print(gi.gi_frame.
