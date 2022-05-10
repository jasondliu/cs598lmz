gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_lasti
# Test gi.gi_frame.f_locals

def f():
    yield 10

# Should not cause f() to be called.
gi = (i for i in f())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_lasti
# Test gi.gi_fram
