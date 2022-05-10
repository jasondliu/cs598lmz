import weakref
# Test weakref.ref objects.

# XXX This should use a list of weakrefs
# to check that no callbacks are triggered by the GC.

class Dummy:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        if self.n > 0:
            print self.n
        else:
            print "Dummy"

class Callback:
    def __init__(self):
        self.called = 0
    def __call__(self, ref):
        self.called = 1

# Create a strong reference to some objects
a = Dummy(1)
b = Dummy(2)
c = Dummy(3)

# Now create a weak reference to a.
cb = Callback()
r = weakref.ref(a, cb)

# Check that r() returns a.
if r() != a:
    raise SystemError, "weakref failed to return original object"

# Check that the callback wasn't called.
if cb.called:
    raise SystemError, "callback called immediately"


