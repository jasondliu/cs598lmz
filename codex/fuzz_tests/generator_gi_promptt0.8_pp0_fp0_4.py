gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    pass
gi = f.gi_frame.gi_code.gi_running
# Test gi.gi_frame.f_code.co_flags

def f():
    pass
gi = f.gi_frame.f_code
# Test gi.gi_frame.f_lasti

def f():
    pass
gi = f.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno

def f():
    pass
gi = f.gi_frame.f_lineno
# Test gi.gi_frame.f_locals

def f():
    pass
gi = f.gi_frame.f_locals
# Test gi.gi_frame.f_trace

def f():
    pass
gi = f.gi_frame.f_trace
# Test gi.gi_frame.f_trace_lines

def f():
    pass
gi = f.gi_frame.f_trace_lines
# Test gi.gi_frame.f_trace_op
