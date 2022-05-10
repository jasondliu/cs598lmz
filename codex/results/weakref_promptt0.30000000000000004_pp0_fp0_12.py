import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)

class C:
    pass

def callback(r):
    print "callback(%s)" % r

def test(obj):
    print "test(%s)" % obj
    r = weakref.ref(obj)
    print "weakref.ref(%s) = %s" % (obj, r)
    print "r() = %s" % r()
    print "r() is obj = %s" % (r() is obj)
    print "r() == obj = %s" % (r() == obj)
    print "r() is None = %s" % (r() is None)
    print "r() == None = %s" % (r() == None)
    del obj
    print "del obj"
    print "r() = %s" % r()
    print "r() is None = %s" % (r() is None)
    print "r() == None = %s" % (r() == None)

def test_callback(obj):
    print
