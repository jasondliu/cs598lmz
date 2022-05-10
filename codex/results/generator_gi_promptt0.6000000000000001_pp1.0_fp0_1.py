gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
assert gi.gi_code is None
assert gi.gi_frame is None
# Test gi.gi_running
assert not gi.gi_running
# Test gi.__next__
try:
    next(gi)
except StopIteration:
    pass
else:
    assert False, "expected StopIteration"

# Test generator.gi_code
def func():
    def gen():
        yield 1
    # Test gen.gi_code
    assert gen.gi_code.co_name == "gen"
    assert gen.gi_code.co_argcount == 0
    assert gen.gi_code.co_flags & CO_GENERATOR
    # Test gen.gi_frame
    assert gen.gi_frame is None
    # Test gen.gi_running
    assert not gen.gi_running
    # Test gen.__next__
    g = gen()
    assert g.gi_code.co_name == "gen"
    assert g.gi_frame.f_code.co_name == "func"

