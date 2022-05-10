gi = (i for i in ())
# Test gi.gi_code, gi_frame, gi_running
assert next.__code__ == gi.gi_code
assert next.__defaults__ == gi.gi_defaults
assert gi.gi_frame is None
assert not gi.gi_running

# Test gi_frame and gi_running.  (Can't test gi_code because
# it's only valid if frame is not None).
def f(gi=gi):
    assert gi.gi_frame is f.__code__.co_firstlineno
    assert gi.gi_running
    next(gi)
    assert gi.gi_frame is None
    assert not gi.gi_running

f()

# Check that gi_frame is set even when the generator immediately exits
def f():
    g = (i for i in ())
    assert g.gi_frame is f.__code__.co_firstlineno
f()

# Check that the gi_frame attribute is not writable
def f():
    g = (i for i in ())
    try:
        g.
