fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This is a bit of a hack, but it lets us use the same test code for both
# CPython and PyPy.
class FakeFrame(object):
    def __init__(self, f_code):
        self.f_code = f_code

