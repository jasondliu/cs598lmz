fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
assert_raises(TypeError, pickle.dumps, fn)

# Test pickle-ability of __code__
def get_code(obj):
    return obj.__code__

for obj in [lambda: None, type(None), int, object]:
    c = get_code(obj)
    assert pickle.loads(pickle.dumps(c)) is c
del c


# Test pickle-ability of __globals__
def get_globals(obj):
    return obj.__globals__

for obj in [lambda: None, type(None), int, object]:
    g = get_globals(obj)
    assert pickle.loads(pickle.dumps(g)) is g
del g


# Exercise the pickling of frames

def test_frame_pickling(frame):
    # Test pickle-ability of frames returned by single calls to getouterframes()
    # and getinnerframes()
    for frame_func in [inspect.getouterframes, inspect.getinnerframes]:
        frames = frame
