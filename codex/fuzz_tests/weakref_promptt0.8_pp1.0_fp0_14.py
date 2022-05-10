import weakref
# Test weakref.ref(WeakKeyDictionary)

class Object(object):

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return '<Object %r>' % (self.key,)

def accept(d):
    print "accepting %r" % (d,)
    print "len(d) =", len(d)
    print "d[key1] = %r, d[key2] = %r" % (d[key1], d[key2])
    print "len(d) =", len(d)
    print "d.keys() =", d.keys()
    print "d.has_key(key1) = %r, d.has_key(key2) = %r" % (d.has_key(key1), d.has_key(key2))
    print "key2 in d = %r" % (key2 in d,)
    print "d.copy() = %r" % (d.copy(),)
    print "d.items() =", d.items()
