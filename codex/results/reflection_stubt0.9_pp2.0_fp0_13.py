fn = lambda: None
gi = (i for i in ())
fn.__code__ = run
gi.gi_frame = fn


def a(i):
    return i
