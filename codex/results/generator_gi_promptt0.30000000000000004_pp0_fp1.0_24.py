gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
gi.gi_frame

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.send()
gi.send(None)

# Test gi.throw()
gi.throw(TypeError)

# Test gi.close()
gi.close()

# Test gi.send() on closed generator
gi.send(None)

# Test gi.throw() on closed generator
gi.throw(TypeError)

# Test gi.close() on closed generator
gi.close()

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno

# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace

# Test gi.gi_frame.f_trace_lines
gi
