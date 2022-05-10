import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

def callback(w):
    print "callback"

def test1():
    print "test1"
    a = []
    a.append(a)
    wr = weakref.ref(a, callback)
    del a
    gc.collect()
    print "test1 end"

def test2():
    print "test2"
    a = []
    a.append(a)
    wr = weakref.ref(a, callback)
    del a
    gc.collect()
    print "test2 end"

def test3():
    print "test3"
    a = []
    a.append(a)
    wr = weakref.ref(a, callback)
    del a
    gc.collect()
    print "test3 end"

def test4():
    print "test4"
    a = []
    a.append(a)
    wr = weakref.ref(a, callback)
    del a
    gc.collect()
    print "test4 end"

def test5
