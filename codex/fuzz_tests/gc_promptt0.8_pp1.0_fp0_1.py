import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on weakrefs of uncollectable objects
# Objects that are not tracked by the garbage collector:
#  int, long, str, unicode, tuple, frozenset
#  instances of user defined types which have no __dict__ or __slots__
#  functions, methods, code objects
#  class objects
#  class instances with no __del__


class C:

    def __del__(self):
        pass


class D(C):
    pass


def showrefs(i, o):
    print '%3d:' % i,
    for ref in gc.get_referrers(o):
        print type(ref),
    print

print 'objects reachable from a single object:'
for i, t in enumerate([object, list, dict, int, str, tuple, set, frozenset,
    C, D]):
    a = t()
    showrefs(i, a)
    del a
    gc.collect()
print

print 'objects reachable from a cycle:'
for i, t in enumerate([list, dict,
