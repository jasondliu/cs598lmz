gi = (i for i in ())
# Test gi.gi_code is None
# Test gi.gi_frame is None
# Test gi.gi_running is False
# Test gi.gi_yieldfrom is None

def gen():
    yield 1
    yield 2
    yield 3

# Test g.gi_code is gen.__code__
# Test g.gi_frame is not None
# Test g.gi_running is False
# Test g.gi_yieldfrom is None
g = gen()

# Test g.gi_code is gen.__code__
# Test g.gi_frame is not None
# Test g.gi_running is False
# Test g.gi_yieldfrom is None
next(g)

# Test g.gi_code is gen.__code__
# Test g.gi_frame is not None
# Test g.gi_running is False
# Test g.gi_yieldfrom is None
next(g)

# Test g.gi_code is gen.__code__
# Test g.gi_frame is not None
# Test g.gi_running is False
# Test g.gi
