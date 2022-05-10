gi = (i for i in ())
# Test gi.gi_code only
assert type(gi.gi_code) is types.CodeType
gi = (i for i in ())
# Test gi.gi_frame
assert isinstance(gi.gi_frame, types.FrameType)
gi = (i for i in ())
# Test gi.gi_weakreflist
assert gi.gi_weakreflist is None

# Frame objects

def test_frame_objects():
    def func(a, b, c=1, d=2, *e, **f):
        return (a, b, c, d, e, f)
    frames = []
    def bar():
        def baz():
            frames.append(sys._getframe())
        baz()
    func(0, d=11, b = 42, e=('x', 'y'), g='spam', k=13)
    bar()
    return frames

f = test_frame_objects()[1]

def test_local_names(frame):
    f_locals = frame.f_locals
    assert f_locals == {'
