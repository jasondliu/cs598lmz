gi = (i for i in ())
# Test gi.gi_code
gi2 = gi.gi_code
gi3 = (i for i in ())
gi4 = gi3.gi_code

# Test gi.gi_frame
def test_gi_frame():
    def f():
        return (i for i in ())
    gi = f()
    gi_frame = gi.gi_frame
    assert gi_frame.f_code is f.func_code

    # Test gi.gi_running
    def f():
        return (i for i in ())
    gi = f()
    assert gi.gi_running is False
    next(gi)
    assert gi.gi_running is True
    try:
        next(gi)
    except StopIteration:
        assert gi.gi_running is False

# Test gi.gi_yieldfrom
def test_gi_yieldfrom():
    def f():
        yield 1
        yield 2
        yield 3
    def g():
        yield from f()
    gi = g()
    next(gi)
    assert gi
