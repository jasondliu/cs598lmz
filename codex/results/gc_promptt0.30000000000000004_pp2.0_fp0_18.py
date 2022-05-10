import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%r)' % self.name
    def __del__(self):
        print 'deleting', self

a = A('a')
b = A('b')
a.b = b
b.a = a
del a, b
gc.collect()

# Test gc.garbage
class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name
    def __del__(self):
        print 'deleting', self

def callback(ignored):
    print 'callback'

c = C('c')
wr = weakref.ref(c, callback)
print 'c:', c
print 'wr:', wr
print 'wr():', wr()
print 'deleting c'
del c
print 'wr():', wr()
print 'gc.garbage
