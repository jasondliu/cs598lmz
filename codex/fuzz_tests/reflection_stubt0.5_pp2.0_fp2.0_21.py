fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    pickle.dumps(fn)
except TypeError:
    pass
else:
    raise RuntimeError("Should have raised TypeError")

class MyFunc(object):
    def __init__(self, code):
        self.__code__ = code

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    pickle.dumps(fn)
except TypeError:
    pass
else:
    raise RuntimeError("Should have raised TypeError")

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    pickle.dumps(MyFunc(gi))
except TypeError:
    pass
else:
    raise RuntimeError("Should have raised TypeError")
