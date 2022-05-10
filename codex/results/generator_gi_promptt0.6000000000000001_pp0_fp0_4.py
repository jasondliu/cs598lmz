gi = (i for i in ())
# Test gi.gi_code.co_freevars
assert gi.gi_code.co_freevars == ()

def f():
    yield

# Test gi_frame.f_locals
assert f().gi_frame.f_locals == {}

def f():
    yield
    yield

# Test gi_frame.f_lasti
assert f().gi_frame.f_lasti == -1

def f():
    yield
    yield

gi = f()
next(gi)

# Test gi_frame.f_lasti
assert gi.gi_frame.f_lasti == 11

def f():
    yield

gi = f()
next(gi)

# Test gi_frame.f_lasti
assert gi.gi_frame.f_lasti == 11

# Test gi_frame.f_locals
assert gi.gi_frame.f_locals == {}

# Test gi_frame.f_trace
assert gi.gi_frame.f_trace is None

# Test gi_frame
