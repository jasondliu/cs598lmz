import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        print 'deleting foo'

def test():
    f = Foo()
    print 'created foo'
    gc.collect()
    print 'collected'

test()

# Test gc.get_referrers()

class Foo:
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        print 'deleting foo'

def test():
    f = Foo()
    print 'created foo'
    print gc.get_referrers(f)
    print gc.get_referrers(f.ref)
    print gc.get_referrers(f.ref())
    print gc.get_referrers(f.ref().ref)
    print gc.get_referrers(f.ref().ref())
    print gc.get_referrers(f.ref
