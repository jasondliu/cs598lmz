import weakref
# Test weakref.ref(c) and
# weakref.ref(a)() == weakref.ref(b)() == weakref.ref(c)() == c

class C(object):
    pass

c = C()

a = weakref.ref(c)
b = weakref.ref(a)

try:
    weakref.ref(a)() == weakref.ref(b)() == weakref.ref(c)()
except TypeError, e:
    print e

# Test that a callable object with a __call__ method can be used as a weak
# callback
class Callable(object):
    def __call__(self, ref):
        self.cb_called = 1

    def check(self):
        if not hasattr(self, 'cb_called'):
            raise RuntimeError, "Callback not invoked"


a = Callable()
wr = weakref.ref(1, a)

# Check that wr() (i.e. wr.__call__()) does not invoke the callback
wr()
a.check()

# Check that the callback
