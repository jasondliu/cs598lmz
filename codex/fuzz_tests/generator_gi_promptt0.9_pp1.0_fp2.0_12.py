gi = (i for i in ())
# Test gi.gi_code.
gi.gi_code == g()
# Test gi.gi_frame.
gi.gi_frame == f()
# Test gi.gi_running.
gi.gi_running
# Test gi.gi_frame.f_code
gi.gi_frame.f_code == g()
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace == None
# Test gi.gi_frame.f_exc_traceback
gi.gi_frame.f_exc_traceback == None
# Test gi.gi_frame.f_exc_type
gi.gi_frame.f_exc_type == None
# Test gi.gi_frame.f_exc_value
gi.gi_frame.f_exc_value == None
# Test gi.gi_frame.f_restricted.


def g():  # this function is called from f()
    pass


def f():
    for i in g
