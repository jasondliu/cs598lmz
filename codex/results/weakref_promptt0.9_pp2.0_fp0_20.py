import weakref
# Test weakref.ref on a weakrefable type with a __del__.
class A(object):

    def __init__(self, value):
        self.value = value
        self.a_ref = None
        self.ref_to_me = None

    def __del__(self):
        global called
        called.append(self.value)
        if self.a_ref is not None:
            assert self.a_ref() is self
        if self.ref_to_me() is not None:
            raise RuntimeError("staying alive")


def callback(a, b, c=1, d=2):
    global called
    called.append(a)
    assert b.value == 5
    assert c == 1
    assert d == 2
    assert b.a_ref() is a
    b.a_ref = None
    assert b.ref_to_me() is b
    b.ref_to_me = None


def f():
    global called
    a = A(1)
    a.ref_to_me = weakref.ref(a, callback
