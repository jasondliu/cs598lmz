gi = (i for i in ())
# Test gi.gi_code.co_filename

# Test for bug #1334791:
# gi_frame is not set for generator functions
# which are not called
def g():
    yield 1

g.gi_frame = None

def test_new_with_frame():
    def f():
        yield 1
    f.gi_frame = None
    g = new_with_frame(f)
    assert g.gi_frame is None
    assert list(g) == [1]
    assert g.gi_frame is None

def test_new_with_frame_2():
    def f():
        yield 1
    f.gi_frame = None
    g = new_with_frame(f, None)
    assert g.gi_frame is None
    assert list(g) == [1]
    assert g.gi_frame is None

def test_new_with_frame_3():
    def f():
        yield 1
    f.gi_frame = None
    g = new_with_frame(f, None, None)
    assert g.gi_frame is
