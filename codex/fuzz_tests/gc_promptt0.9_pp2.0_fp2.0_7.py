import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
l1 = []
l2 = []
class C(object):
    def __del__(self):
        l2.append(1)
        l1.append(C())
        del l1[:]
c = C()
l1.append(c)
 l1.append(c)
del c
gc.collect()
len(l1), len(l2)
class Counter(object):
    def __init__(self):
        self.count = 0
    def __repr__(self):
        return repr(self.count)
    def __call__(self):
        self.count += 1
counters = [Counter() for i in range(10)]
counters.append(counters)
del counters
len(gc.garbage)
len(gc.garbage)
gc.garbage[-1].append(gc.garbage)
del gc.garbage
gc.collect()
del l2[:]
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
del l2[:]
gc.set_
