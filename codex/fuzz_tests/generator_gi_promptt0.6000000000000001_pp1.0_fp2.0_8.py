gi = (i for i in ())
# Test gi.gi_code.co_flags
# CO_GENERATOR, CO_ITERABLE_COROUTINE

gi = (i for i in ())
gi.gi_frame.f_lasti
# Test gi_frame.f_lasti
# -1

gi = (i for i in ())
gi.gi_frame.f_trace
# Test gi_frame.f_trace
# None

gi = (i for i in ())
gi.gi_frame.f_trace_lines
# Test gi_frame.f_trace_lines
# None

gi = (i for i in ())
gi.gi_frame.f_trace_opcodes
# Test gi_frame.f_trace_opcodes
# None

gi = (i for i in ())
gi.gi_frame.f_lineno
# Test gi_frame.f_lineno
# 1

gi = (i for i in ())
gi.gi_frame.f_back
# Test gi_frame.f_back
# None

gi = (i for i in ())
gi.gi_
