import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()
print "start"
class C(object):
    def __del__(self):
        print "C is dying"

# create object reference to the object
o = C()
# create a weak reference to the object
# so that it is kept alive
w = weakref.ref(o)

# create a weak reference to the object
# so that it is kept alive
# w = weakref.ref(o)

print "   refcount(o) ==", sys.getrefcount(o)
print "   refcount(w) ==", sys.getrefcount(w)
print "   w() ==", w()

# trigger collection of 'o'
# del o
o=None
print "   collect"
gc.collect()

# weak reference is still alive
print "   w() ==", w()

# create a strong reference to 'o' again
o = w()
print "   refcount(o) ==", sys.getrefcount(o)


# trigger collection of 'o'
del o
print "   collect"
