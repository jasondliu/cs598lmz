import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs
class Foo:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return 'Foo(%d)' % self.i

def test():
    lst = []
    for i in range(10):
        f = Foo(i)
        lst.append(f)
    for f in lst:
        print f
    print 'Collecting...',
    gc.collect()
    print 'done.'
    for f in lst:
        print f
    print 'Collecting...',
    gc.collect()
    print 'done.'
    for f in lst:
        print f
    print 'Collecting...',
    gc.collect()
    print 'done.'
    for f in lst:
        print f
    print 'Collecting...',
    gc.collect()
    print 'done.'
    for f in lst:
        print f
    print 'Collecting...',
    gc.collect()
    print 'done.'
    for f
