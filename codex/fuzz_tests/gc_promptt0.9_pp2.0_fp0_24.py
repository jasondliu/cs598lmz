import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.garbage
print 'Testing...'
ob = object()
print type(ob)
print '**** initial garbage listing:'
print gc.garbage
l = []
l.append(l)
print '**** after creating self-referent list:'
print gc.garbage
del l
print '**** after del l:'
print gc.garbage
print '**** collecting:'
gc.collect()
print '**** after collect:'
print gc.garbage
print 'done'

print "\ntesting gc.get_objects"
import weakref
def object_graph(obj):
    d = {}
    def visit(o):
        r = weakref.ref(o)
        if r in d:
            return
        d[r] = None
        yield r

    # perform a pre-order traversal of object graph
    pending = [obj]
    while pending:
        current = pending.pop()
        for r in visit(current):
            if r() is not None:
                pending.append(r())
                yield (r, current)



