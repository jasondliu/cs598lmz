gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test gi.__name__
gi.__name__
# Test gi.__qualname__
gi.__qualname__

# Test gi.send(1)
gi.send(1)
# Test gi.throw(TypeError)
try:
    gi.throw(TypeError)
except TypeError:
    pass
# Test gi.close()
gi.close()
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lineno

# Test gi.send(1)
gi.send(1)
# Test gi.throw(TypeError)
try:
    gi.throw(TypeError)
except TypeError:
    pass
# Test g
