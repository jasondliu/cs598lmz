import weakref
# Test weakref.ref()
# Test weakref.proxy()
# Test weakref.getweakrefcount()
# Test weakref.getweakrefs()

class C:
    pass

def callback(x):
    print "callback called with", x

def test_callback():
    c = C()
    r = weakref.ref(c, callback)
    del c
    gc.collect()
    print "callback should have been called"

def test_basic():
    c = C()
    r = weakref.ref(c)
    print r() is c
    del c
    gc.collect()
    print r() is None

def test_basic_callback():
    c = C()
    r = weakref.ref(c, callback)
    print r() is c
    del c
    gc.collect()
    print "callback should have been called"

def test_callback_with_argument():
    c = C()
    r = weakref.ref(c, callback, "extra argument")
    del c
    gc.collect()
    print
