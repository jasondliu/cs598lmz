gi = (i for i in ())
# Test gi.gi_code.co_flags.
gi.gi_code.co_flags
gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_flags.
gi.gi_frame.f_code.co_flags
gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_lasti
def f():
    for i in range(5):
        gi.gi_frame.f_locals['i'] = i
f()
gi
# Test gi_frame.f_lineno
gi.gi_frame.f_code.co_firstlineno
gi
gi.gi_frame.f_code
gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_filename
gi.gi_frame.f_code.co_firstlineno
gi.gi_frame.f_code.co_firstlineno
gi
gi.gi_frame.f_lineno
gi.gi_frame.f_lineno
gi.gi_frame.f_lin
