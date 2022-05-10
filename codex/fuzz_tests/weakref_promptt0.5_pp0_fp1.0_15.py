import weakref
# Test weakref.ref
import gc

class C:
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "C.__del__"

def test_ref():
    c = C(1)
    r = weakref.ref(c)
    print "ref", r
    print "ref.a", r().a
    print "ref.a", r().a
    del c
    gc.collect()
    print "ref.a", r().a # should raise an exception

# Test weakref.proxy

def test_proxy():
    l = []
    class C:
        def __init__(self, a):
            self.a = a
            l.append(self)
        def __del__(self):
            print "C.__del__"
    c = C(1)
    p = weakref.proxy(c)
    print "proxy", p
    print "proxy.a", p.a
    print "proxy.a", p.a
    del c
    gc.
