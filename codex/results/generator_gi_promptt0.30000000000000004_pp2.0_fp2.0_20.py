gi = (i for i in ())
# Test gi.gi_code is a function object
assert isinstance(gi.gi_code, types.CodeType)
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is False
assert gi.gi_running is False
# Test gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None

# Test gi.gi_frame is a frame object
def f():
    gi = (i for i in ())
    assert isinstance(gi.gi_frame, types.FrameType)
f()

# Test gi.gi_running is True
def f():
    gi = (i for i in ())
    next(gi)
    assert gi.gi_running is True
f()

# Test gi.gi_yieldfrom is a generator object
def f():
    gi = (i for i in ())
    yield from gi
    assert isinstance(gi.gi_yieldfrom, types.GeneratorType)
f()

# Test gi_code.co_filename
