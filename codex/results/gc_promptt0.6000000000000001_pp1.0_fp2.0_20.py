import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_referrers()

# A simple class with a few special methods.
class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(' + self.name + ')'
    def __del__(self):
        print 'deleting', self

print 'gc.collect()'
gc.collect()
print

print 'c = C(name=c)'
c = C('c')
print 'gc.collect()'
gc.collect()
print 'gc.get_referrers(c) =', gc.get_referrers(c)
print

print 'l = [c]'
l = [c]
print 'gc.collect()'
gc.collect()
print 'gc.get_referrers(c) =', gc.get_referrers(c)
print

print 'l2 = [c2]'
c2 = c
l2 = [c2]
print 'gc.collect()'
gc.collect()
