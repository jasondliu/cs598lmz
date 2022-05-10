gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame on generator iterator (fixes #4971)
assert gi.gi_code is gi.__next__.__code__
assert gi.gi_frame is None

def f():
    return (i for i in range(5))

gi = f()
# Test gi.gi_code and gi.gi_frame on generator iterator (fixes #4971)
assert gi.gi_code is f.__code__
assert gi.gi_frame is None
