import weakref
# Test weakref.ref() with callbacks
import _weakref

class C:
    def __init__(self, v):
        self.v = v

    def __repr__(self):
        return "C(%s)" % self.v

    def callback(self, r):
        print("ref(%s) to C(%s)" % (r, self.v))


def f(v):
    c = C(v)
    p = weakref.ref(c, lambda r: c.callback(r))
    print("p = %s" % p)
    return p


# test weakref.ref()'s callback

def test_callback():
    p = f(5)
    print("p() = %s" % p())
    del p
    import gc
    gc.collect()
    print("del p; gc.collect()")


# test weakref.ref.__del__
def test_del():
    c = C(10)
    p = weakref.ref(c, lambda r: c.callback(r))
   
