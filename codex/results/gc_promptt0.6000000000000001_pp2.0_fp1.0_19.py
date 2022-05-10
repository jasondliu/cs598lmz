import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print 'deleting', self.x

f = Foo(1)
print 'collecting'
gc.collect()
print 'done'

f = Foo(2)
print 'collecting'
gc.collect()
print 'done'

f = Foo(3)
print 'collecting'
gc.collect()
print 'done'

f = Foo(4)
print 'collecting'
gc.collect()
print 'done'
# Test gc.garbage
class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print 'deleting', self.x

f = Foo(1)
print 'collecting'
gc.collect()
print 'garbage contains:', gc.garbage
print 'done'

f = Foo(2)
print 'collecting'
gc.collect()
print 'garbage contains:', gc
