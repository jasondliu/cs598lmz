gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test gi.__name__

# Test gi.send
# Test gi.throw
# Test gi.close

# Test gi.__iter__
# Test gi.__next__

# Test gi.gi_frame
# Test gi.gi_code

# This is needed to test gi.gi_frame and gi.gi_code.
# (The function itself is not tested here.)
def frame_and_code():
    yield

gi = frame_and_code()
next(gi)

# Test gi.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno
# Test gi.gi_frame.f_builtins
# Test gi.gi_frame.f_globals
# Test gi.gi_frame.f_locals

# Test gi.gi_frame.f_back
# Test gi.gi_frame.f_
