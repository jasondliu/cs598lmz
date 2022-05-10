import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, and test weakref-based callback list.
# Also exercises objects that must be tracked by the collector.
class G(object):
    pass
glist = []
class C(object):
    def __init__(self):
        self.x = G()
        self.wref = weakref.ref(self)
    def __del__(self):
        glist.append(self.wref)
    def callback(self, w):
        glist.append(w)
c = C()
wr = weakref.ref(c, c.callback)
gid = id(G())
del c, C
# XXX weakrefs can apparently trigger gc several times before they all
# disappear
gc.collect(); gc.collect(); gc.collect(); gc.collect()
for i in xrange(10):
    if len(glist)==2 and glist[0]() is None:
        break
    gc.collect(); gc.collect(); gc.collect(); gc.collect()
else:
    raise TestFailed, "didn't collect everything immediately"
