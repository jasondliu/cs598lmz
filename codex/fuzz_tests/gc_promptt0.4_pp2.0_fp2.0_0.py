import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
r = weakref.ref(o)
print r
print r()

# Test weakref.getweakrefs()
print weakref.getweakrefs(o)

# Test weakref.proxy()
print weakref.proxy(o)

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
d[o] = 1
print d

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[1] = o
print d

# Test weakref.WeakSet()
s = weakref.WeakSet()
s.add(o)
print s

# Test weakref.WeakMethod()
class Foo:
    def bar(self):
        print "bar"

f = Foo()
m = weakref.WeakMethod(f.bar)
print m
m()

# Test weakref.finalize()
o = object()
f = weakref.finalize(o, lambda ref: print "dying",
