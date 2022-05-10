gi = (i for i in ())
# Test gi.gi_code is dead in this case, but
# that gi.gi_frame is alive.
def test_generator_gi_frame_threshold(self):
    # This threshold is 10 by default.  It's a
    # little wibbly, because there's not a clean
    # way to force a collection without triggering
    # a gc.collect().
    def f():
        yield 1
    g = f()
    g.next()
    for i in xrange(11):
        assert g.gi_frame
    gc.collect()
    assert g.gi_frame
    gc.collect()
    assert g.gi_frame is None

def test_generator_finalization(self):
    # If a generator is not collected, its frame survives.
    # Its code object will be kept alive by the code object
    # cache.
    def f():
        yield 1
    g = f()
    g.next()
    # A bit of a hack:  the code object lives in the
    # f_code of the frame, which lives in g.gi_frame.
