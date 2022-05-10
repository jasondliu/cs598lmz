gi = (i for i in ())
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_running

gi = (i for i in (1))
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_running

gi = (i for i in (1,))
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_running

def f():
    return (i for i in (1,))
gi = f()
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_running

def f():
    return (i for i in (1,2))
gi = f()
# Test gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
# Test gi.gi_
