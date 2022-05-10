import weakref
# Test weakref.ref() with Cyclic Garbage Collection and an
# explicit finalizer.
import gc, weakref

def finalizer(nr, wlist=[]):
    for i in range(len(wlist)):
        if wlist[i]() is None:
            print "item", i, "has died"
        else:
            print "item", i, "is still alive"
    print "finalizer %d executed" % nr
def callback(nr, wlist=[]):
    print "callback %d executed" % nr

#

class C:
    pass
o = C()
w = weakref.ref(o, finalizer)
w2 = weakref.ref(o, callback)
w3 = weakref.ref(o)
wlist = [w, w2, w3]
o.attr = wlist

print "\nthree weak references to", o
print "w:", w
print "w2:", w2
print "w3:", w3

del o
print "\ndeleted o"

print "\ngc.collect()
