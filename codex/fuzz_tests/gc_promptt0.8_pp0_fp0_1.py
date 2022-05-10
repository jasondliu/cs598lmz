import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
x = weakref.WeakValueDictionary()
# weakref.proxy()
# Test proxies
p = weakref.proxy(x)
class C:
    pass
c = C()
#prox = weakref.proxy(c)
# Test references
r = weakref.ref(c)
# Test callbacks
def callback(arg):
    print "Callback called with", arg
    print "refcount =", sys.getrefcount(arg)
    print "hash =", hash(arg)
    print "proxy =", weakref.proxy(arg)
    print

def create_cycle():
    l = []
    l.append(l)
    return l

x = create_cycle()
#cref = weakref.ref(x, callback)
#print "Created weak reference cref"
#print "sys.getrefcount(x) =", sys.getrefcount(x)
#print "cref =", cref
#print "cref() =", cref()
#print "cref() is x", cref() is x
