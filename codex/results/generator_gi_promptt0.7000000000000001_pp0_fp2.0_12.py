gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_running
# check that gi.gi_code is the same as the code attribute of the
# generator iterator
def g():
    yield
gi = g()
next(gi)
assert gi.gi_code is g.__code__
# check that gi.gi_frame is the same as the frame attribute of the
# generator iterator
def g():
    yield
gi = g()
next(gi)
assert gi.gi_frame is g.__code__
# check that gi_running is true while the generator is running and
# false otherwise
def g():
    yield
gi = g()
next(gi)
assert gi.gi_running
next(gi)
assert not gi.gi_running
# check that gi_running is false for a newly-created generator
def g():
    yield
gi = g()
assert not gi.gi_running
# check that gi_running is false for a generator that terminated
# normally
def g():
    return
gi = g()
next(gi)
assert
