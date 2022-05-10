import weakref
# Test weakref.ref(C())
assert_raises(TypeError, weakref.ref, C())

# Test weakref.ref(self)
class D(object):
    def __init__(self):
        self.wr = weakref.ref(self)
    def __del__(self):
        pass
weakref.ref(D())

# Test del self inside a __del__ method
class E(object):
    def __init__(self, cb):
        self.wr = weakref.ref(self, cb)
    def __del__(self):
        del self.wr
weakref.ref(E(None))

# Test that creating a cycle causes a __del__ method to be called
# immediately
# XXX This test is disabled because it causes the test suite to crash
# on some platforms (OS X).  I don't know why.
def test_crash():
    class F(object):
        def __init__(self):
            self.wr = weakref.ref(self)
        def __del__(self):
            pass
    f = F()

