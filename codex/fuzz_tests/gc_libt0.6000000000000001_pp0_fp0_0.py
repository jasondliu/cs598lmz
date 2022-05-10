import gc, weakref

class C(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print self.x, 'deleted'


# A weakref with a callback
c = C(1)
r = weakref.ref(c, lambda x: print('callback', x))
print 'r:', r
print 'c:', c
print 'r():', r()
print 'deleting c'
del c
print 'r():', r()

# A weakref without a callback
c = C(2)
r = weakref.ref(c)
print 'r:', r
print 'c:', c
print 'r():', r()
print 'deleting c'
del c
print 'r():', r()

# A weakref to a list
c = C(3)
l = [c]
r = weakref.ref(l)
print 'r:', r
print 'l:', l
print 'r():', r()
print 'deleting c'
del c
print
