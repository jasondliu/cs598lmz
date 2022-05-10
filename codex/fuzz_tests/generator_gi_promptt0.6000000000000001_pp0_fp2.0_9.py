gi = (i for i in ())
# Test gi.gi_code.co_name
gi.gi_code.co_name
# Test gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_name
# Test gi.gi_frame.f_back.f_code.co_name
gi.gi_frame.f_back.f_code.co_name

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    gi.gi_frame.f_code.co_name

f()

# Test gi.gi_frame.f_back.f_code.co_name
def f():
    gi = (i for i in ())
    gi.gi_frame.f_back.f_code.co_name

f()

# Test gi.gi_code.co_name
def f():
    gi = (i for i in ())
    gi.gi_code.co_name

f()

# Test gi.gi_frame.f
