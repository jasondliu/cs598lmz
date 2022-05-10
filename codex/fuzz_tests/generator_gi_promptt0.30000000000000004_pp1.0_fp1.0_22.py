gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & CO_GENERATOR

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 1

# Test gi.gi_frame.f_trace
def tracefunc(frame, event, arg):
    return tracefunc

gi.gi_frame.f_trace = tracefunc
assert gi.gi_frame.f_trace(gi.gi_frame, 'call', None) is tracefunc

# Test gi.gi_frame.f_exc_traceback
try:
    raise ValueError
except ValueError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    gi.gi_frame.f_exc_traceback = exc_tb
    assert gi.gi_frame.f_exc_traceback is exc_tb

# Test gi.gi_
