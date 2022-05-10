gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals

# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace

# Test gi.gi_running
gi.gi_running

# Test gi.send
gi.send(None)

# Test gi.throw
gi.throw(TypeError)

# Test gi.close
gi.close()

# Test gi.gi_frame.f_back
gi.gi_frame.f_back

# Test gi.gi_frame.f_builtins
gi.gi_frame.f_builtins

# Test gi.gi_frame.f_code
gi.gi_frame.f_code

# Test gi.gi_frame.f_globals
gi.gi
