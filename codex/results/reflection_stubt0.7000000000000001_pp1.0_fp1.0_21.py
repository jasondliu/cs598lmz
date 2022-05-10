fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    dill.detect.badtypes.detect(fn)
    assert False
except TypeError:
    pass

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    dill.detect.badtypes.detect(fn)
    assert False
except TypeError:
    pass

fn = lambda: None
gi = (i for i in ())
fn.__closure__ = (gi,)
try:
    dill.detect.badtypes.detect(fn)
    assert False
except TypeError:
    pass

fn = lambda: None
gi = (i for i in ())
fn.__defaults__ = (gi,)
try:
    dill.detect.badtypes.detect(fn)
    assert False
except TypeError:
    pass


class A(object):
    __slots__ = ['foo', 'bar']

    def __init__(self, foo=1, bar=2):
        self.foo = foo
        self.bar = bar
