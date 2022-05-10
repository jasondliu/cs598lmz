import weakref
# Test weakref.ref() for objects of dynamically allocated types.
class C(object):
    pass

def f():
    x = C()
    x.y = C()
    x.y.z = C()
    wr = weakref.ref(x.y.z)
    print "\nBefore clearing y"
    print "Reference object:", wr
    print "Object referenced:", wr()
    print "deleting x..."
    del x
    print "After clearing y"
    print "Reference object:", wr
    print "Object referenced:", wr()

f()
