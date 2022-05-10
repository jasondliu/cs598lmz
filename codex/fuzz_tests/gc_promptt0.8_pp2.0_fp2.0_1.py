import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in tp_clear()
# - collect() has no effect there, but it should not crash
# - issue #8432: the test used to crash

class C(object):
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print 'C.__del__(%d)' % self.n

# generate a few gc-tracked cycles, to split the freelists
for i in xrange(10):
    x = C(i)
    y = C(i)
    y.x = x
    x.y = y

all_instances = []
all_instances_set = set()

def get_new_instance():
    obj = C(len(all_instances))
    all_instances.append(obj)
    all_instances_set.add(obj)
    gc.collect()
    return obj

def callback(ignored):
    # collect() shouldn't crash even when tp_clear is called
    print 'got callback'
    gc.collect
