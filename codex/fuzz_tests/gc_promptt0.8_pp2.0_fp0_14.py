import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on various forms of cycles.
# Weakrefs are used to keep track of whether objects are still alive.


class P(object):
    pass


class Q(P):
    pass


class C(object):
    pass


class D(C):
    pass


w = weakref.WeakKeyDictionary()


def check():
    gc.collect()
    w.clear()
    for o in gc.get_objects():
        if isinstance(o, (P, C)):
            w[o] = None


def make_graph(n):
    # Build a directed acyclic graph with n nodes, numbered
    # 0 to n-1.
    nodes = [None] * n
    for i in range(n):
        nodes[i] = P()
    check()
    for src in range(n):
        dst = (src * 577) % n
        nodes[src].child = nodes[dst]
        check()
    return nodes


print('Objects in graph:', len(w))
print('Collecting graph
