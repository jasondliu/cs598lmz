import weakref
# Test weakref.ref(instance) with a cyclic reference.
#
# This test demonstrates that cyclic references don't prevent
# instance from being deleted.

class C:
    pass

def f():
    o = C()
    o.cycle = o
    return o

o = f()
o_wr = weakref.ref(o)
o = None
print(o_wr)

if gc.isenabled():
    print("running gc")
    gc.collect()
    print(o_wr)
    print("running gc")
    gc.collect()
    print(o_wr)
