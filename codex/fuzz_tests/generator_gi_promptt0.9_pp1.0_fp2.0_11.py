gi = (i for i in ())
# Test gi.gi_code is the function
eq(gi.gi_code, (i for i in ()).__next__.__code__)
gi = (i for i in ())
# Test gi.gi_frame is a frame
assert isinstance(gi.gi_frame, types.FrameType)
gi = (i for i in ())
# Test gi.gi_running is 0
eq(gi.gi_running, 0)

# Test created genexpr is an instance of GeneratorType
assert isinstance((i for i in ()), GeneratorType)

# Test that the closure for a created genexpr contains the genexpr
gi = (i for i in ())
eq(gi.gi_frame.f_locals['gi'], gi)

# Test iter(gi) is gi
gi = (i for i in ())
# Test stopiteration raised from gi.next() call
try:
    gi.__next__()
except StopIteration:
    pass

# Test created genexpr has func_defaults
gi = (i for i in ())
eq(gi.__closure__[1].cell
