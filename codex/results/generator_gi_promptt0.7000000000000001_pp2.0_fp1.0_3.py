gi = (i for i in ())
# Test gi.gi_code is None

# Test gi.gi_frame is None

# Test gi.gi_running is False
def f():
    yield 1
g = f()
# Test g.gi_code is f.__code__

# Test g.gi_frame is not None

# Test g.gi_running is False

# Test g.gi_frame.f_back is None

# Test g.gi_frame.f_code is g.gi_code

# Test g.gi_frame.f_lasti is 0

# Test g.gi_frame.f_lineno is 1

# Test g.gi_frame.f_locals is g.gi_frame.f_globals

# Test g.gi_frame.f_trace is None

# Test g.gi_frame.f_exc_traceback is None

# Test g.gi_frame.f_exc_type is None

# Test g.gi_frame.f_exc_value is None
g.next()
# Test g.gi_frame.f_lasti is 7
