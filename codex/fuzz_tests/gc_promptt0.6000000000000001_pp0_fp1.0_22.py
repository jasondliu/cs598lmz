import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class C(object):
    pass

def callback(w):
    print 'callback', w

# test weak refs

c = C()
w = weakref.ref(c, callback)
w2 = weakref.ref(c)

print 'before'
gc.collect()
print 'after'

del c
gc.collect()

# test weak callable refs

class D(object):
    def __call__(self):
        pass

d = D()
wr = weakref.ref(d)
print wr() is d
print wr() is wr()

del d
gc.collect()

# test weak method refs

class E(object):
    def spam(self):
        pass

e = E()
wr = weakref.ref(e.spam)
print wr() is e.spam
print wr.__self__ is e
print wr() is wr()

del e
gc.collect()

# test a weakref that references an instance method

class F(object):
    def
