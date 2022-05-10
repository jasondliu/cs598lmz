import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

def show_refs(name, ob):
    print '%s id=%s:' % (name, id(ob)),
    print ', '.join([x for x in gc.get_referrers(ob)
                    if isinstance(x, dict)])

def dump_garbage():
    print '\nGARBAGE:'
    gc.collect()
    print '\nGARBAGE OBJECTS:'
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:77] + '...'
        print type(x), '\n  ', s

a = A()
show_refs('a', a)
dump_garbage()

b = B()
show_refs('b', b)
dump_garbage()

c = C()

