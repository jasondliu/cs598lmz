fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


def to_raise(e):
    raise e

class ReprWrapper(Exception):
    def __init__(self, obj):
        self.obj = obj
    def __repr__(self):
        return repr(self.obj)

