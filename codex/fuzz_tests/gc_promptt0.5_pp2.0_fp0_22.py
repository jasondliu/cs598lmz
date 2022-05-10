import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    for i in range(10):
        x = C()

def g():
    for i in range(10):
        x = C()
        y = weakref.ref(x)

#print gc.collect()

#f()
#print gc.collect()

#g()
#print gc.collect()

# Test weakref.ref(x, callback)

#def refcallback(x):
#    print "callback", x
#
#def f():
#    x = C()
#    y = weakref.ref(x, refcallback)
#    x.attr = 1
#    x = 1
#
#f()
#print gc.collect()

class C:
    pass

def f():
    x = C()
    x.attr = 1
    x = 1

def g():
    x = C()
    x.attr = 1
    y = weakref.ref(x)
    x = 1

#f()
#print
