import weakref
# Test weakref.ref(a=1, b=2)

def f():
    o = lambda : None
    o.a = 1
    o.b = 2
    r = weakref.ref(o)
    ok(r() is o and r().a == 1 and r().b == 2,
       "weakref.ref(a=1, b=2) works as expected")

    ok(repr(r) == '<weakref at 0x%x; to "function" at 0x%x>' % \
       (id(r), id(o)),
        "weakref.ref(a=1, b=2) has expected repr output")

test(f, "Test weakref.ref(a=1, b=2)")
