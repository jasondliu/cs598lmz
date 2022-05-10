gi = (i for i in ())
# Test gi.gi_code.co_name.
gi.gi_code.co_name

# Test gi.gi_frame.f_code.co_name.
def f():
    yield
gi = f()
gi.gi_frame.f_code.co_name

# Test gi.gi_frame.f_globals["__name__"].
def f():
    yield
gi = f()
gi.gi_frame.f_globals["__name__"]

# Test gi.gi_frame.f_locals["__name__"].
def f():
    yield
gi = f()
gi.gi_frame.f_locals["__name__"]

# Test gi.gi_frame.f_back.f_code.co_name.
def f():
    def g():
        yield
    gi = g()
    return gi.gi_frame.f_back.f_code.co_name
f()

# Test gi.gi_frame.f_back.f_globals["__name__"].
def f
