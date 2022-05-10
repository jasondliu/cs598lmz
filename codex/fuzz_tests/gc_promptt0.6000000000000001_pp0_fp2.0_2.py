import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

#
# Test weakrefs to objects with a __del__ method
#

class C(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x
    def __del__(self):
        print 'C.__del__'

class D(object):
    def __init__(self, y):
        self.y = y
    def __repr__(self):
        return 'D(%r)' % self.y
    def __del__(self):
        print 'D.__del__'

class E(C):
    def __del__(self):
        print 'E.__del__'
        super(E, self).__del__()

gc.collect()
gc.collect()
gc.collect()

print 'creating some objects...'
c = C(1)
d = D(2)
e = E(3)

