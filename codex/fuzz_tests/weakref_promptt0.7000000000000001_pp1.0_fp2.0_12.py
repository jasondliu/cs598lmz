import weakref
# Test weakref.ref(list) on large lists

def test():
    print "testing weakref.ref(list)...",
    refs = []
    for i in xrange(10000):
        x = [0, 1]
        refs.append(weakref.ref(x))
    del x
    for r in refs:
        assert r() is None
    print "OK"

test()
