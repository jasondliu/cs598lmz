gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_trace
def tracer(frame, event, arg):
    print(frame, event, arg)
    return tracer
gi.gi_frame.f_trace = tracer

# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno

# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals

# Test gi.gi_frame.f_globals
gi.gi_frame.f_globals

# Test gi.gi_frame.f_code
gi.gi_frame.f_code

# Test gi.gi_frame.f_back
gi.gi_frame.f_back

# Test gi.gi_frame.f_builtins
gi.gi_frame.f
