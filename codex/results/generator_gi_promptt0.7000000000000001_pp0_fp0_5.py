gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame.
gi.gi_code
gi.gi_frame
# Test gi.gi_running.
gi.gi_running
# Test gi.gi_yieldfrom.
gi.gi_yieldfrom

# Test property gi.gi_frame.
gi.gi_frame
# Test property gi.gi_code.
gi.gi_code
# Test property gi.gi_running.
gi.gi_running
# Test property gi.gi_yieldfrom.
gi.gi_yieldfrom

# Test attribute gi.__name__.
gi.__name__
# Test attribute gi.__qualname__.
gi.__qualname__
# Test attribute gi.__annotations__.
gi.__annotations__
# Test attribute gi.__dict__.
gi.__dict__
# Test attribute gi.__weakref__.
weakref.proxy(gi)

# Test method gi.close.
gi.close()
# Test method gi.send.
gi.send(1)
#
