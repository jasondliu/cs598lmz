gi = (i for i in ())
# Test gi.gi_code.co_flags
try:
    gi.gi_code.co_flags
    print("FAILED: generator gi_code.co_flags not hidden")
except AttributeError:
    print("OK: generator gi_code.co_flags hidden")

# Test gi.gi_frame.f_trace
# FIXME: Second half of this test disabled for now. See issue #162.
#try:
#    gi.gi_frame.f_trace
#    print("FAILED: generator gi_frame.f_trace not hidden")
#except AttributeError:
#    print("OK: generator gi_frame.f_trace hidden")
try:
    gi.gi_frame.f_trace_lines
    print("FAILED: generator gi_frame.f_trace_lines not hidden")
except AttributeError:
    print("OK: generator gi_frame.f_trace_lines hidden")
try:
    gi.gi_frame.f_trace_opcodes
    print("FAILED: generator gi_frame.f
