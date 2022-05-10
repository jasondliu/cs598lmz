import gc, weakref

obj = Object()
c = weakref.ref(obj)
print obj, c, c()  # make sure gc doesn't fire too soon
assert c() is obj
print obj, c, c()
del obj 
print c
try:
    c()
    assert False
except:
    print "It happened, as expected"

w = weakref.WeakKeyDictionary()
for i in xrange(10):
    obj = Object()
    w[obj] = 1
    print obj, c, c()  # make sure gc doesn't fire too soon

gc.collect()

for obj in w:
    assert obj is not None
    assert w[obj] == 1
