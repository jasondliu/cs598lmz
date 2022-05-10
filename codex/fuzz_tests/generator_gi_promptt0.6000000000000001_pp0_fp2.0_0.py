gi = (i for i in ())
# Test gi.gi_code.co_flags, since it's the only one that can't be set by
# the user.
print(gi.gi_code.co_flags & CO_GENERATOR)

# Test gi.gi_frame.f_trace
def g():
    yield 1
    yield 2

gi = g()
next(gi)
gi.gi_frame.f_trace = lambda *args: None
gi.gi_frame.f_trace(gi.gi_frame, 'line', None)
