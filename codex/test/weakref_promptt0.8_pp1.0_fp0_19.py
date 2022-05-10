import weakref
# Test weakref.ref() with callbacks
import _weakref


class MyException(Exception):
    pass


# Create callback
class Callback:
    def __init__(self):
        self.called = False

    def __call__(self, ref):
        self.called = True


def callback(ref):
    pass


# Create tests

def test_instancemethod():
    global cb
    cb = Callback()
    x = Foo()
    ref = weakref.ref(x, cb)
    del x
    support.gc_collect()
    assert cb.called, "callback not called"


def test_lambda():
    global cb
    cb = Callback()
    x = Foo()
    ref = weakref.ref(x, lambda r: cb())
    del x
    support.gc_collect()
    assert cb.called, "callback not called"


def test_function():
    global cb
    cb = Callback()
    x = Foo()
    ref = weakref.ref(x, callback)
