gi = (i for i in ())
# Test gi.gi_code.
gi.gi_code
# Test gi.gi_frame.
gi.gi_frame
gi.gi_frame.f_lineno
gi.gi_frame.f_lasti
gi.gi_frame.f_code
gi.gi_frame.f_code.co_filename
# Test gi.gi_running, gi.gi_frame, gi.gi_code, gi.gi_yieldfrom.
def f():
    gi = (i for i in range(5))
    # Test gi.gi_running.
    gi.gi_running
    # Test gi.gi_frame.
    gi.gi_frame
    # Test gi.gi_code.
    gi.gi_code
    # Test gi.gi_yieldfrom.
    gi.gi_yieldfrom
    gi.send(None)
    gi.gi_frame
    gi.gi_code
    gi.gi_frame.f_lasti
f()
