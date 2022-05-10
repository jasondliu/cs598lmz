import weakref
# Test weakref.ref(obj) does not cause any leaks.
import gc
import objgraph


class A(object):
    pass
obj = A()
wref = weakref.ref(obj)
del obj
gc.collect()
objgraph.show_most_common_types()
