import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

def f(x):
    print "entering f..."
    a = A()
    print "leaving f..."

def f2():
    print "entering f2..."
    a = A()
    a.a = A()
    print "leaving f2..."

def f3():
    print "entering f3..."
    a = A()
    c = weakref.ref(a)
    a.a = A()
    print "leaving f3..."

def f4():
    print "entering f4..."
    a = A()
    c = weakref.ref(a)
    a.a = A()
    a = None
    print "leaving f4..."

def f5():
    print "entering f5..."
    a = A()
    c = weakref.ref(a)
    a.a = A()
    a = None
    gc.collect()
    print "leaving f5..."

def f6():
    print "ent
