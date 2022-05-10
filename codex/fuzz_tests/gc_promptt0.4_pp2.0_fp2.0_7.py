import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def callback(x):
    print 'callback:', x

class A:
    def __init__(self):
        self.callback = lambda x: callback(x)

a = A()
a.callback(1)
wref = weakref.ref(a, lambda x: callback(x))
del a
gc.collect()

# Test gc.get_referrers()
l = [1, 2, 3]
a = A()
a.callback(l)
a.callback = lambda x: callback(x)
a.callback(l)
a.callback = l
a.callback(l)
a.callback = l[:]
a.callback(l)
a.callback = l.append
a.callback(4)
a.callback = l.count
a.callback(1)
a.callback = l.extend
a.callback([4])
a.callback = l.index
a.callback(1)
a.callback = l.insert
a.callback(0, 1)
a.callback = l.pop
a.callback()

